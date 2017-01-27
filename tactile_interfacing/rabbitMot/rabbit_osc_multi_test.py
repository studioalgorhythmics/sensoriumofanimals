# -*- coding: utf-8 -*-
##################################################
'''
control multiple DRV2605 using muiltiple I2C multiplexar TCA9548
control via OSC
'''
##################################################

import OSC

import time
import threading


from Adafruit_DRV2605 import *
from Adafruit_I2C_mod import Adafruit_I2C

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

#for I2C devices
TCA9548_addr = 0x70 # 0x70 by default pin setting. up to 0x77
TCA9548_num = 2 #number of multiplexer
i2c_dev_num = 10; #number of devices connected to TCA9548

TCA9548_li = []
drv_li = []

print TCA9548_addr

for m in range(TCA9548_num):
    print TCA9548_addr+m
    TCA9548_li.append(Adafruit_I2C(TCA9548_addr+m, busnum=2, debug=False))
    
TCA9548_li[0].writesimple(1<<(0)) #change channel on TCA9548
#TCA9548_li[1].writesimple(0)
drv_li.append(Adafruit_DRV2605(busnum=2))
#TCA9548_li[0].writesimple(0)
TCA9548_li[1].writesimple(1<<(0)) #change channel on TCA9548
drv_li.append(Adafruit_DRV2605(busnum=2))

TCA9548_li[0].writesimple(1<<(0)) #change channel on TCA9548
#TCA9548_li[1].writesimple(0)
drv_li[0].begin()
drv_li[0].selectLibrary(1)
drv_li[0].setMode(DRV2605_MODE_INTTRIG)
#TCA9548_li[0].writesimple(0)
TCA9548_li[1].writesimple(1<<(0)) #change channel on TCA9548
drv_li[1].begin()
drv_li[1].selectLibrary(1)
drv_li[1].setMode(DRV2605_MODE_INTTRIG)


def mot_do_ind(mot_id,effect):
    if mot_id == 0:
        print mot_id
        TCA9548_li[0].writesimple(1<<0)
        #TCA9548_li[1].writesimple(0)
        drv_li[0].setWaveform(0, int(effect))
        drv_li[0].setWaveform(1, 0)
        drv_li[0].go()
    elif mot_id == 1:
        print mot_id
        #TCA9548_li[0].writesimple(0)
        TCA9548_li[1].writesimple(1<<0)
        drv_li[1].setWaveform(0, int(effect))
        drv_li[1].setWaveform(1, 0)
        drv_li[1].go()
    else :
        return

    '''
    for n in range(i2c_dev_num):
        TCA9548_li[m].writesimple(1<<(n%8)) #change channel on TCA9548
        drv_li.append(Adafruit_DRV2605(busnum=2))
    '''
'''    
for m in range(TCA9548_num):
    for n in range(i2c_dev_num):
        TCA9548_li[m].writesimple(1<<(n%8)) #change channel on TCA9548
        drv_li[n].begin()
        drv_li[n].selectLibrary(1)
        drv_li[n].setMode(DRV2605_MODE_INTTRIG)
'''
'''
#drive indiviual motor for multiple multiplexer
def mot_do_ind_multi(mot_id,effect):
    m_index = mot_id/8
    TCA9548_li[m_index].writesimple(1<<(mot_id%8))
    drv_li[mot_id].setWaveform(0, int(effect))
    drv_li[mot_id].setWaveform(1, 0)
    drv_li[mot_id].go()
'''


'''
for n in range(i2c_dev_num):
    TCA9548 = Adafruit_I2C(TCA9548_addr, busnum=2)
    TCA9548.writesimple(1<<n) #change channel on TCA9548
    drv_li.append(Adafruit_DRV2605(busnum=2))
'''

'''
#prepare DRV2605 on multiplexer
for n in range(i2c_dev_num):
    TCA9548.writesimple(1<<n)
    drv_li[n].begin()
    drv_li[n].selectLibrary(1)
    drv_li[n].setMode(DRV2605_MODE_INTTRIG)
'''



'''
#drive indiviual motor
def mot_do_ind(mot_id,effect):
    TCA9548.writesimple(1<<mot_id)
    drv_li[mot_id].setWaveform(0, int(effect))
    drv_li[mot_id].setWaveform(1, 0)
    drv_li[mot_id].go()
'''     

