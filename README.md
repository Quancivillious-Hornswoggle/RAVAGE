# RAVAGE: A linux shell tool

Directions: paste commands in shell in order

`git clone https://github.com/Meta-bhsc/RAVAGE.git`

`cd RAVAGE`

`sudo apt install tor`

`sudo pip install -r requirements.txt`

`to run: sudo python RAVAGE.py`

*SUDO IS NEEDED IN ALL COMMANDS*
## 
### Error Fix:
If you get the error saying b'liblibc.a' is not found run these two commands and then you should be able to run it

`cd /usr/lib/x86_64-linux-gnu/`

`sudo ln -s -f libc.a liblibc.a`

Then now just run RAVAGE
##

### Available Tools:

- Instagram Scraper
- Phisher
- Network Scanner
- Port Scanner
- Packet Sniffer
- Web Scraper
- Wifi Flooder

## UPDATES
- Updated the network scanner to scan all the possible hosts
- Updated all of the letters to numbers in the selection menus
- Added Wifi Flooder
- Added Mac Address and IP Address changer when using the network full scan, and a wifi flooder
- Added TOR proxy connection when running the tool
## NOTES
- When using the wifi flooder make sure to get the mac address of the ip being flooded. The wifi flooder is meant to be used after using the network scanner
