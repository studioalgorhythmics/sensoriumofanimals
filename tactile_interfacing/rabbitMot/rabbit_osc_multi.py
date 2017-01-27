# -*- coding: utf-8 -*-
##################################################
'''
for Beaglebone green
control multiple DRV2605 using muiltiple multiplexar TCA9548 
control via OSCseq
'''
##################################################

import OSC

import time
import threading


from Adafruit_DRV2605 import *
from Adafruit_I2C_mod import Adafruit_I2C

##OSC
#OSC server
osc_server_address = ("192.168.7.2", 9000)
osc_server = OSC.OSCServer(osc_server_address)
osc_server.addDefaultHandlers()

def oscSeqhandler(addr,tag, args,src):
    print "addr: " + str(addr) + " tag: " + str(tag) + " args: " + str(args) + " src: " + str(src)
    print "id:" + str(args[0]) + " effect: " + str(args[1])
    mot_do_ind_multi(args[0],args[1]);
    
def pinghandler(addr,tag, args,src): #suppress crazy ping from OSCseq
    #print "addr: " + str(addr) + " tag: " + str(tag) + " args: " + str(args) + " src: " + str(src)
    return

osc_server.addMsgHandler('/mot', oscSeqhandler )
osc_server.addMsgHandler('/ping', pinghandler )
osc_server_thread = threading.Thread(target=osc_server.serve_forever)
osc_server_thread.start()

##I2C
#for I2C devices
TCA9548_addr = 0x70 # 0x70 by default pin setting. up to 0x77
TCA9548_num = 2 #number of multiplexer
i2c_dev_num = 10; #number of devices connected to TCA9548

TCA9548_li = []
drv_li = []

#init
for m in range(TCA9548_num):
    TCA9548_li.append(Adafruit_I2C(TCA9548_addr+m, busnum=2))
    for n in range(8):
        try:
            TCA9548_li[m].writesimple(1<<n) #change channel on TCA9548
            drv_li.append(Adafruit_DRV2605(busnum=2))
        except:
            print "e"

print "init: " + str(len(TCA9548_li)) + " multiplexer " + str(len(drv_li)) + " drv";

#begin
for m in range(TCA9548_num):
    for n in range(8):
        try:
            TCA9548_li[m].writesimple(1<<n) #change channel on TCA9548
            drv_li[n+(m*8)].begin()
            drv_li[n+(m*8)].selectLibrary(1)
            drv_li[n+(m*8)].setMode(DRV2605_MODE_INTTRIG)
        except:
            print "e"

#drive indiviual motor for multiple multiplexer
def mot_do_ind_multi(mot_id,effect):
    try:
        m_index = mot_id/8
        TCA9548_li[m_index].writesimple(1<<(mot_id%8))
        drv_li[mot_id].setWaveform(0, int(effect))
        drv_li[mot_id].setWaveform(1, 0)
        drv_li[mot_id].go()
    except:
        print "e"
        return

