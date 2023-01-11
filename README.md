## Make a QR code generator.
For make a QR Code, QR Code module must be installed first.
- Download the latest [Python installer](https://www.python.org/downloads/) for your OS.
I used [this website](https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=Reinstall%20Python%20to%20Fix%20'Pip,components%20to%20fix%20the%20problem.) for help, you can have a look if you want.
-  Users who want to use pip for installing the QR Code module on Windows in the command prompt have to use the command:
```
pip install qrcode
```
We enter whatever we want to define in the QR code, we write it in ' img = qrcode.make('linkOrOther') '.
After the generate, we write the name and extension of the image in ' img.save('lastNameQRCode.jpg') '.

![](/iLoveThisPlaylist.jpg)

