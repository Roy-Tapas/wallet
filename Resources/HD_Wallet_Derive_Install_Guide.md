# HD-Wallet-Derive Install Guide

This guide serves as a step by step process for setting up the [`hd-wallet-derive` library](https://github.com/dan-da/hd-wallet-derive) used to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins or "altcoins."

The `hd-wallet-derive` library is written in the PHP language; therefore, you will be required to first set up PHP on your machines before installing and then running the `hd-wallet-derive` library.

You can follow the step by step video guides in the following links.

<details><summary>Microsoft Windows Users</summary>

* [Installing PHP Version 7.3 for Windows](https://youtu.be/IvcZZaIEL_4)

* [HD Derive Wallet Install for Windows](https://youtu.be/A_tqm4j4vsY)

</details>

<details><summary>macOS Users</summary>

* [Installing PHP Using the Homebrew Package Manger for Mac](https://youtu.be/SNRQSwlOKbs)

* [HD Derive Wallet Install for Mac](https://youtu.be/c-Qc3Pss6oM)

</details>


## Step 2 - Installing hd-wallet-derive 

With the latest version of PHP installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.

<details><summary>Installation</summary>

1. Begin by opening a fresh terminal. Windows users **must** open their terminal as administator as follows:

    * Input `C:\Program Files\Git\bin\bash.exe` directly into the system search bar and launch the program as _Administrator_ from the resulting menu. 
    
    * **This step is required or the installation will fail!**

    * <img alt=bash-exe.png src=Images/bash-exe.png height=500>

2. With your terminal open as indicated for your operating system, cd into your `Blockchain-Tools folder and run the following code:

    ```shell
      git clone https://github.com/Roy-Tapas/wallet
      cd hd-wallet-derive
      curl https://getcomposer.org/installer -o installer.php
      php installer.php
      php composer.phar install
    ```

3. You should now have a folder called `hd-wallet-derive` containing the PHP library!

