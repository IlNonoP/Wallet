
# Wallet

Welcome! This is a program written in python that allows you to securely save keys and passwords so that a script can access them using the appropriate library! The keys are encrypted and only the ROOT user can access them, effectively making them very secure. There are various levels of security, which include access alerts, confirmations and notifications, or even sha code verification and md5 plus directory verification, making unauthorized access very difficult

## Features

- Create/Request/Delete keys
- Verification of the requesting file directory
- Verification of the sha1 and md5 code of the requesting file
- Appearance of a pop-up to request a password to secure access, complete with name and location of the requesting file
- Appearance of access alert notifications
- Pop-up to approve access


## Installation

Installation is really easy, just have python installed on your system, download the repository, enter the Source folder and start the installation file!

```bash
  git clone https://github.com/IlNonoP/Wallet.git
  cd Wallet
  cd Source
  sudo bash install.sh
```

The installer will create the necessary directories in the /opt/wallet folder, they will be the only ones used by the program. You will also create a sh file that executes with sudo without asking for the password, this file starts the wallet, and is called by a second file that is started at startup. The.desktop file is copied to the /home/[user]/.confing/autostart folder so that it runs at startup. After installation, reboot is required


## Usage/Examples
### Put a key in the wallet
First of all you need to download the WalletRequests file [https://github.com/IlNonoP/Wallet/blob/main/WalletRequests.py].

It should then be placed in the same directory as your python program and imported as a library.


```python
import WalletRequests
```

Now we can create our own key

```python
import WalletRequests
WalletRequests.put_key("NAME", "KEY", "ID", "SECURITY_OPTION", "PASSWORD")
```
Let's see the options in more detail:

- NAME = name of the key, you need something unique to avoid duplications, be original, and remember that it is the name of the key, if you forget it you can say goodbye to your key!
- KEY = the data you need to save safely
- ID = is your identifier, it's as if it were a password, it's data that shouldn't be shared if security options aren't selected, but you can also leave it if you use other authentication methods
- SECURITY_OPTIONS = These are the security options, they can be combined in different ways. They will be explained in detail in a specific chapter
- PASSWORD = If you have enabled the password, enter it here, if you have not enabled it, leave the quotes with a space or write whatever you want, it will be an ignored field

#### Security options
Security options are digits that are placed in the appropriate field when creating the key, these are the available options:

- 0 = Only ID verification: Use only the ID for verification, if it is present all other checks are skipped even if set

- 1 = Same file directory: Verify that the request comes from the same location as the one who created the key, then verify that the file directory and name match

- 2 = Sha1: Check whether the sha1 code of the file that will request the key is the same as the one that created it

- 3 = Md5: Check whether the md5 code of the file that will request the key is the same as the one that created it

- 4 = Passowrd: Asks for the specified password when a program wants to access the key

- 5 = Show notification: A 3-second notification appears saying which key is about to be read and by whom

- 6 = Request visual confirmation: A confirmation pop-up appears for key access

Security options can be combined however you want, and are used when creating the key to tell the program what it needs to take into account during verification

example:
```python
import WalletRequests
WalletRequests.put_key("ServerDecryptKey", "ABCD1234", "user", "123456", "password1")
```

Please note: If 0 is entered all checks will be skipped and only the ID will count

### Get a key from the wallet
Withdrawing the key is even easier
```python
import WalletRequests

key = WalletRequests.get_key("NAME", "ID")
print(key)
```

In this case you only need ID and Key Name, ID as verification and name to know which key you need to access

When you try to read the key you will be asked for the checks set during creation, if even one fails the key will not be shown

### Remove a key from the wallet
Removing is even easier!
```python
import WalletRequests

WalletRequests.remove_key("NAME", "ID")
```
In this case you only need ID and Key Name, ID as verification and name to know which key you need to remove

When you try to remove the key you will be asked for the checks set during creation, if even one fails the key will not be shown

## Support

For support, email IlNonoP@outlook.it or open an issues on GitHub

