#!/usr/local/bin/python3
# coding=utf8
import os, pyshark, pythonosc, argparse, time
from pythonosc import osc_message_builder
from pythonosc import udp_client

iface = "wlan1"
#ch = "6"

os.system("ifconfig " + iface + " down") 
os.system("iwconfig " + iface + " mode monitor")
os.system("ifconfig " + iface + " up")
#os.system("iwconfig " + iface + " channel " + ch)

# PYSHARK Capture init
capture = pyshark.LiveCapture(interface=iface)
capture.sniff_continuously()

def PacketHandler(pkt):

	try:
		pkt['wlan']
	except KeyError:
		print("Not a wlan packet")
	else:
		#check if it is an acces point
		if pkt['wlan'].fc_type == "0" and pkt['wlan'].fc_subtype == "8" :
			print("Station - MAC: " + pkt['wlan'].sa 
				+ " Signal: " + pkt['radiotap'].dbm_antsignal
				+ " Channel: " + pkt['radiotap'].channel_freq
				+ " SSID: " +  pkt['wlan_mgt'].ssid)
		#or check if it is a client
		elif pkt['wlan'].fc_type == "0" and pkt['wlan'].fc_subtype == "4" :
			print("Client - MAC: " + pkt['wlan'].sa
				+ "")

# Pkt listener
capture.apply_on_packets(PacketHandler)

### For channel hopping (doesn't work properly)
# while True:
# 	for channel in range(1, 14):
# 		os.system("iwconfig " + iface + " channel " + str(channel))
# 		print ("\r\n~~~ Sniffing on channel " + str(channel) + " ~~~")
# 		start = time.time()
# 		capture = pyshark.LiveCapture(interface=iface)
# 		capture.sniff(timeout=2)
# 		end = time.time()

# 		for pkt in capture.sniff_continuously(packet_count=10):
# 			#capture.apply_on_packets(PacketHandler)
# 			PacketHandler(pkt)

# 		#capture.apply_on_packets(PacketHandler)
# 		#capture.sniff(packet_count=10)
# 		# for pkt in capture:
# 		# 	#capture.apply_on_packets(PacketHandler)
# 		# 	PacketHandler(pkt)


# 		#time.sleep(1)