##################################################

##################################################

import time

from Adafruit_DRV2605 import *
from Adafruit_I2C_mod import Adafruit_I2C

TCA9548_addr = 0x70 # 0x70 to 0x77 I2C address of multiplexer
i2c_dev_num = 2; #how many devices (motor) on TCA9548
drv_li = [] #list (array) of motor object

# initalize 
for n in range(i2c_dev_num):
    TCA9548 = Adafruit_I2C(TCA9548_addr, busnum=2) #multiplexer 
    TCA9548.writesimple(1<<n)#change channel of TCA9548 using bytecode for example 000000001 and then 00000010
    drv_li.append(Adafruit_DRV2605(busnum=2)) #store first slave driver/channel to list

# effect number
effect = 17
    
# setup     
for n in range(i2c_dev_num):
    TCA9548.writesimple(1<<n)
    drv_li[n].begin()
    drv_li[n].selectLibrary(1)
    drv_li[n].setMode(DRV2605_MODE_INTTRIG)
    
    
### loop ### 
while(True):
    print("Effect #" + str(effect))

    for n in range(i2c_dev_num):
        TCA9548.writesimple(1<<n)
        drv_li[n].setWaveform(0, effect)
        drv_li[n].setWaveform(1, 0) #end? see Adafruit DRV2605 arduino library?
        drv_li[n].go()
        time.sleep(1); #sleep between individual motors in sec for ms in float for example 0.1 = 100ms
    
    # wait a bit
    time.sleep(1)#sleep after all connected motors are driven in sec
    
''' go through effect library 
    effect+=1
    if(effect > 117):
        effect = 1
    # end if(effect
'''
# end while(True)
