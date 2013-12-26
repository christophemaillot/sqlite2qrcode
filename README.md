#sqlite2qrcode
A simple python script that reads a Google Secrets sqlite database, and generate de TOTP qrcode images from accounts found in this database.

Usefull for restoring the Google Secrets accounts from a backup database.

## requirements
You need at least the following python packages :

* sqlite
* qrcode
* pil

## usage
```
sqlite2qrcode ./databases
```
will read the ./databases sqlite file and generate QRCode images in the current directory.








