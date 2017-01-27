# -*- coding: utf-8 -*-
##################################################
'''
control multiple DRV2605 using I2C multiplexer TCA9548
control via OSCseq www.oscseq.com
'''
##################################################

import OSC
import time
import threading

from Adafruit_DRV2605 import *
from Adafruit_I2C_mod import Adafruit_I2C

###OSC 
#OSC server
osc_server_address = ("192.168.7.2", 9000)
osc_server = OSC.OSCServer(osc_server_address)
osc_server.addDefaultHandlers()


def oscSeqhandler(addr,tag, args,src):
    print "addr: " + str(addr) + " tag: " + str(tag) + " args: " + str(args) + " src: " + str(src)
    print "id:" + str(args[0]) + " effect: " + str(args[1])
    mot_do_ind(args[0],args[1]);
    


def pinghandler(addr,tag, args,src):#suppress crazy ping from OSCseq
    #print "addr: " + str(addr) + " tag: " + str(tag) + " args: " + str(args) + " src: " + str(src)
    return

osc_server.addMsgHandler('/mot', oscSeqhandler )
osc_server.addMsgHandler('/ping', pinghandler )
osc_server_thread = threading.Thread(target=osc_server.serve_forever)
osc_server_thread.start()

###I2C device
#for I2C devices
TCA9548_addr = 0x70 # 0x70 by default pin setting. up to 0x77
i2c_dev_num = 4; #number of devices connected to TCA9548

drv_li = []


for n in range(i2c_dev_num):
    TCA9548 = Adafruit_I2C(TCA9548_addr, busnum=2)
    TCA9548.writesimple(1<<n) #change channel on TCA9548
    drv_li.append(Adafruit_DRV2605(busnum=2))

#prepare DRV2605 on multiplexer
for n in range(i2c_dev_num):
    TCA9548.writesimple(1<<n)
    drv_li[n].begin()
    drv_li[n].selectLibrary(1)
    drv_li[n].setMode(DRV2605_MODE_INTTRIG)

#drive indiviual motor
def mot_do_ind(mot_id,effect):
    print "do "+" mot_id: " + str(mot_id) + " effect " + str(effect)
    TCA9548.writesimple(1<<mot_id)
    drv_li[mot_id].setWaveform(0, int(effect))
    drv_li[mot_id].setWaveform(1, 0)
    drv_li[mot_id].go()
        

