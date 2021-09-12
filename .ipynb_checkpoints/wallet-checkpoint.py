# Import dependencies
import os
import subprocess
import json
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
from eth_account import Account
from web3.middleware import geth_poa_middleware
from web3 import Web3
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

cryptos =[ETH,BTCTEST]
numderive=3
coins = {}

# Create a function called `derive_wallets`
def derive_wallets(mnem,coin,numderive):
    command = f'php ./derive -g --mnemonic="{mnem}" --coin="{coin}" --numderive={numderive} --cols=address,index,privkey,pubkey --format=json' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
for crypto in cryptos:
    coins[crypto] = derive_wallets(mnemonic,crypto,numderive)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,priv_key):
    if coin == ETH:
        account =  Account.privateKeyToAccount(coins[coin][0]['privkey'])
    elif coin == BTCTEST:
        account =  PrivateKeyTestnet(coins[coin][0]['privkey'])
    else:
        pass
    return account

ETH_account = priv_key_to_account(ETH, coins[ETH][0]['privkey'])
BTCTEST_account = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        return {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gas": gasEstimate,
            "gasPrice": w3.eth.gasPrice,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address,[(recipient, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin,account,recipient, amount):
    tx = create_tx(coin, account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result.hex()
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)