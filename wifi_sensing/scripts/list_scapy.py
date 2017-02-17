#!/usr/local/bin/python3
# coding=utf8
import os
from scapy.all import *

#here is your interface in monitor mode
iface="wlan1"

os.system("ifconfig " + iface + " down") 
os.system("iwconfig " + iface + " mode monitor")
os.system("ifconfig " + iface + " up")

station_list = []
client_list = []

def PacketHandler(pkt) :

	if pkt.haslayer(Dot11) :
		#print(pkt.command())
		#check if it's a station
		if pkt.type == 0 and pkt.subtype == 8 :
			#check mac address for redundancy
			#if pkt.addr2 not in station_list :
				#station_list.append(pkt.addr2) 
				print("Station - MAC: " + str(pkt.addr2).strip() +" Signal: "+ str(pkt.db_antsignal) +" SSID: " + str(pkt.info).strip('b\''))
		#or check if it's a client
		elif pkt.type == 0 and pkt.subtype == 4 :
			#check mac address for redundancy
			#if pkt.addr2 not in client_list :
				#client_list.append(pkt.addr2)
				print("Client - MAC: " + str(pkt.addr2).strip() + " Probe: " + str(pkt.info).strip('b\''))


#sniff(iface=iface, prn = PacketHandler)


while True:
	for channel in range(1, 14):
		os.system("iwconfig " + iface + " channel " + str(channel))
		print ("Sniffing on channel " + str(channel))

		sniff(iface=iface, prn=PacketHandler, count=10, timeout=1, store=0)
		time.sleep(1)