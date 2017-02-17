#WiFi Sensing

Scan WiFi stations and clients with a BBGW with TP-Link TL-WN722N, using aicrack-ng (part 1, not stable yet) or scapy (part 2, only getting MAC addresses and SSIDs and printing them in the console for the moment).
Visualize them with p5.js on any machine with a web browser and node.js (part 3).

All of the following is executed on a BBGW running Debian, through ssh, by default: `ssh debian@192.168.7.2`

##Part 1: Using Aircrack-ng

Scan WiFi stations and clients with airodump-ng, stream them live through OSC from a BBGW with TP-Link TL-WN722N dongle. 

Install aircrack-ng
```
sudo apt-get update
sudo apt-get install aircrack-ng
```

Put your WiFi interface into monitor mode (`wlan1` is your interface identifier, might be different, use `ifconfig` if not sure)
```
sudo airmon-ng start wlan1
```
If using TL-WN722N, green led shoud blink while into monitor mode.


Start scanning WiFi stations and clients (`-o csv -w dump writes to a CSV file with "dump" prefix)
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

##Part 2: Using Scapy

Install scapy

```
pip3 install scapy-python3
```
The list_scapy.py script takes charge of putting your interface in monitor mode (wlan1 by default, might be different, use `ifconfig` if not sure), then it hops on 2.4GHz channels and sniffs 802.11 packets. Requires `sudo` to put interface in monitor mode and sniff packets.
```
sudo python3 list_scapy.py
```
So far list_scapy.py prints the data in the console, should send them through OSC in the future.

##Part 3: Visualize with p5.js
Coming soon.