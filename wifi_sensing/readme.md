#WiFi Sensing

Scan WiFi stations and clients with airodump-ng, stream them live with OSC and visualize them with p5.js.

##Aircrack-ng

Install aircrack-ng
~~~~
sudo apt-get update
sudo apt-get install aircrack-ng
~~~~

Put your WiFi interface into monitor mode (where wlan0 is your interface, might me different)
~~~~
airmon-ng start wlan0
~~~~

Start scanning WiFi stations and clients (-o writes only CSV file)
~~~~
airodump-ng -o csv -w dump mon0
~~~~
This should create a dumpXX.csv file, be sure to do it in the __same folder__ which is being used by the python script.

##Python and OSC

Install python 3, pip, python-osc
~~~~
sudo apt-get install python3 python3-pip
sudo pip3 install python-osc
~~~~

##p5.js