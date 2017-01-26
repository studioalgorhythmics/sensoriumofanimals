_/_/_/_/Read me_/_/_/_/
ver 160125
Akitoshi Honda

_/_/Intriduction_/_/
Python 2.x code with beagle bone green for motor control with Adafruit I2C multiplexer TCA9548 and DRV2605 motor driver

_/_/Requirement_/_/
_/_/_/Software_/_/_/
(not preinstalled)
-Python smbus
To install do following command in terminal (need internet connection)
	sudo apt-get update
	sudo apt-get install python-smbus
(Pre installed on beagle bone green)
-Python 2.x
-Flask

_/_/_/Hardware_/_/_/
Beagle bone green
Adafruit TCA9548
Adafruit DRV2605
Proper actuator(motor)

_/_/File directory_/_/
RabbitMot
	├── Adafruit_DRV2605.py		prerquired. Python library for DRV2605
	├── Adafruit_I2C_mod.py		prerquired. Python library for I2C
	├── basic_multi2.py			basic motor control without WebUI
	├── rabbit_webui.py			basic motor control with WebUI
	└── templates
    		└── index.html		html template for WebUI

_/_/how to use_/_/

1. copy RabbitMot to beablebone
2. Build hardware on breadboard 
3. run Basic multi2.py in cloud9/terminal (check usb ports and check address with i2cdetect -r -y 2 (in cloud9/ terminal)


RabbitWebUI

1. Start rabbit_webui.py (from cloud9) (check and change i2c_dev_num) 
2. Open http://192.168.7.2:5000/ from browser on the pc which beagle bone is connected
3. Full fill the fields and push send button
	Start: default 0
	Effect: int 1-116
	Duration: float in seconds. If you want 200ms, fill 0.2
	Interval: pause after all motors are driven. You can set also 0. 
4. To stop, set start to 0 and press send.
Don’t send string. It will crash.




