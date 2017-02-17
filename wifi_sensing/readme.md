#WiFi Sensing

Scan WiFi stations and clients with a BBGW with TP-Link TL-WN722N, using aicrack-ng (part 1, not stable yet) or scapy (part 2, scanning on one channel only).
Visualize them with p5.js on any machine with a web browser and node.js.

All of the following is executed on a BBGW running Debian, through ssh, to access by default: `ssh debian@192.168.7.2`

##Using Aircrack-ng

Scan WiFi stations and clients with airodump-ng, stream them live through OSC from a BBGW with TP-Link TL-WN722N dongle. 

Install aircrack-ng
```
sudo apt-get update
sudo apt-get install aircrack-ng
```

Put your WiFi interface into monitor mode (`wlan1` is your interface identifier, might be different)
```
sudo airmon-ng start wlan1
```
If using TL-WN722N, green led shoud blink while into monitor mode.


Start scanning WiFi stations and clients (`-o csv -w dump` writes to a CSV file with "dump" prefix)
```
sudo airodump-ng -o csv -w dump mon0
```
This should create a dumpXX.csv file, be sure to do it in the __same folder__ which is being used by the python script.

###Python & OSC

Install python 3, pip, python-osc
```
sudo apt-get install python3 python3-pip
sudo pip3 install python-osc
```
_list_wifi.py_ reads the last dumpXX.csv from airodump-ng and sends the values through OSC to an IP address and port. Think to change theses values in the script depending on what you want.
```
python3 list_wifi.py
```

###Screen
You should use `screen` to run airmon-ng and .py script at the same time and see what's going on.
See how to use it [here](http://aperiodic.net/screen/quick_reference).

##Using Scapy

Install scapy

```
pip3 install scapy-python3
```

##p5.js