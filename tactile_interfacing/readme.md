#Read me 
A project by Akitoshi Honda in collaboration with Studio ALgorhythmics.

##Introduction
Python 2.x code for beagle bone green to do motor control with Adafruit I2C multiplexer TCA9548 and DRV2605 motor driver.


##Requirements
###Software (not preinstalled)
* Python smbus
	* To install do following command in terminal (need internet connection)
	* sudo apt-get update
	* sudo apt-get install python-smbus
* (Pre installed on beagle bone green)
	* Python 2.x
	* Flask

###Hardware
- Beagle bone green
- Adafruit TCA9548
- Adafruit DRV2605
- Proper actuator(motor)

##How to use

1. copy RabbitMot to beablebone
2. Build hardware on breadboard 
	* see rabbit_moto.fzz and rabbit_moto_bb.pdf in this folder 
3. run Basic multi2.py in cloud9/terminal 
	# check usb ports and check address with i2cdetect -r -y 2 (in cloud9/ terminal)


###RabbitWebUI

1. Start rabbit_webui.py (from cloud9) (check and change i2c_dev_num) 
2. Open http://192.168.7.2:5000/ from browser on the pc which beagle bone is connected
3. Full fill the fields and push send button
	- Start: default 0
	- Effect: int 1-116
	- Duration: float in seconds. If you want 200ms, fill 0.2
	- Interval: pause after all motors are driven. You can set also 0. 
4. To stop, set start to 0 and press send.
- Don’t send string. It will crash.




