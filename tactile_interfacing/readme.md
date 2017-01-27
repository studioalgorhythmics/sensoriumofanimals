##Introduction
A project by Akitoshi Honda in collaboration with Studio Algorhythmics.

Python 2.x code for [beagle bone green](http://wiki.seeed.cc/BeagleBone_Green_Wireless/) to do motor control with [Adafruit I2C multiplexer TCA9548](https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/overview) and [DRV2605 motor driver](https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/overview).


##Requirements
###Software (not preinstalled)
* Python smbus
	* To install do following command in terminal (need internet connection)
	* `sudo apt-get update`
	* `sudo apt-get install python-smbus`
* Pre installed on beagle bone green
	* Python 2.x
	* Flask

###Hardware
- See rabbit_moto.fzz and rabbit_moto_bb.pdf in this folder for wiring/ circuit
- Components:
	- Beagle bone green
	- Adafruit TCA9548
	- Adafruit DRV2605
	- Proper actuator(motor)


##How to use

1. Copy the folder "RabbitMot" to [beaglebone](http://beagleboard.org/getting-started) using Cloud9
2. Build hardware on breadboard 
	* see rabbit_moto.fzz and rabbit_moto_bb.pdf in this folder 
3. Run python scripts in the folder "RabbitMot" in Cloud9/terminal 
	# check usb ports (sometimes they don't have enough power/current) and check if address of drivers are detected with `i2cdetect -r -y 2` (in cloud9/ terminal)


##Scripts
###basic_multi2.py
- Basic testing with general parameters and an example for setting up with a simple loop.


###rabbit_webui.py
- Start "rabbit_webui.py" in the folder "RabbitMot" from Cloud9. Check and change i2c_dev_num. 
- Open http://192.168.7.2:5000/ from browser on the pc connected to the beagle bone board.
- Fill-in the fields and push send button or "enter".
	- Start: default 0
	- Effect: int 1-116
	- Duration: float in seconds. If you want 200ms, fill 0.2
	- Interval: pause after all motors are driven. You can set also 0. 
	- Don’t send strings. It will crash.
- To stop, set start to 0 and press send.

###rabbit_osc.py
- requires python package [pyosc](https://pypi.python.org/pypi/pyOSC) install on the [beaglebone](http://beagleboard.org/getting-started) using Cloud9/terminal with 'sudo pip install pyosc'
- simple [osc/open sound control](https://en.wikipedia.org/wiki/Open_Sound_Control) receiver used in conjuction with a osc sender. We used [OSCseq](http://oscseq.com/manual/) for testing. 



