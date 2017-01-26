# -*- coding: utf-8 -*-
##################################################
'''
control multiple DRV2605 using I2C multiplexar TCA9548
GUI with Flask
to open GUI, connect http://192.168.7.2:5000/ via browser
don't forget fullfill the fields
'''
##################################################

import time
import threading

import datetime

from Adafruit_DRV2605 import *
from Adafruit_I2C_mod import Adafruit_I2C

from flask import Flask, render_template, request, redirect, url_for

today = datetime.date.today()


#for I2C devices
TCA9548_addr = 0x70 # 0x70 by default pin setting. up to 0x77
i2c_dev_num = 2; #number of devices connected to TCA9548
drv_li = []

#prepare TCA9548
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

#for WebUI and control motor
mot_start=0; #0 off 1 = on
effect=17;
duration=1; #sleep between individual motors in sec
interval=1; #sleep between all connected motors

#for debug
pre_time=0;
now_time=0;

#drive the motor
def mot_do2(): #duration as parameter
    for n in range(i2c_dev_num):
        TCA9548.writesimple(1<<n)
        drv_li[n].setWaveform(0, int(effect))
        drv_li[n].setWaveform(1, 0)
        drv_li[n].go()
        print "mot_"+str(n)+":"+str(effect)
        time.sleep(float(duration));
        
#timer loop for cotinuous motor driving loop (threading)       
def loop_timer():
    global mot_start
    
    global effect
    global duration
    global interval
        
    #print "mot_start:" + str(mot_start)
    #print("current thread num: " + str(threading.activeCount()))
    #print("[%s]" % threading.currentThread().name)
    '''
    global now_time
    global pre_time
    now_time = time.time() - pre_time
    pre_time = time.time()
    print now_time
    '''
    if int(mot_start) == 1: #motor drive on
        print "thread_timer_interval:" + str(interval)
        mot_do2() #do function above 
    '''
    elif int(mot_start) == 0: #motor drive off
        print "thread ignored"
    else:
        print "none"
    '''
    #print "interval:" + str(interval)
    t=threading.Timer(float(interval),loop_timer)
    t.start()

#for WebUI 
app = Flask(__name__)
# what happens when access at root
@app.route('/')
def index():
    # render index.html
    return render_template('index.html')

#waht happens whan access /post
@app.route('/post', methods=['GET', 'POST'])
def post():
    
    global mot_start
    global effect
    global duration
    global interval
        
    if request.method == 'POST':
        mot_start = request.form['start']
        effect = request.form['effect']
        duration = request.form['duration']
        interval = request.form['interval']
        #print "post:s" + mot_start + "e:"+ effect + "d:" + duration + "i" + interval
        
        return render_template('index.html',start=mot_start,effect=effect,duration=duration,interval=interval)
    else:
       return 0
#main
if __name__ == '__main__':
    #start thread for timer loop
    t=threading.Thread(name="main_thread",target=loop_timer)
    t.start()
    #start WebUI. You can change host, if needs.
    app.debug = True 
    app.run(host='192.168.7.2')
    