# Fan controlled by temperature

## Overview

The project consists of a fan attached to a DC motor. 
The temperature and humidity senzor will send data to the program.
The program can be called with 2 command line arguments representing the option (temperature or humidity) and the limit.
This motor will start spinning when the temperature or humidity is higher than the limit imposed by the user.

## Gif demo

![gif_demo](https://github.com/at-cs-ubbcluj-ro/solo-project-dogoPaprika/blob/master/media/ezgif.com-gif-maker.gif)

For starting the program I type ```python3 prj.py temp 33```
This means the program will compare the temperature with 33 degrees. As seen in the demo, when temperature is below 33, the output will be green and the motor will stop spinning if it was turned on previously. When is above 33,
the output will be red and the motor starts spinning. When there is no output from the sensor (connection is unstable) the output is blue and the motor stops. I heated the sensor with a hair dryer so the temperature will rise and humidity will decrease.
You can also call the program with ```hum``` argument instead of ```temp```.

## Schematics plan

![fritzing_schema](https://github.com/at-cs-ubbcluj-ro/solo-project-dogoPaprika/blob/master/media/fritzing_schema.png)

## Pre-requisites

* [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* Jumping wires
* Breadboard 
* [DC motor](https://components101.com/motors/toy-dc-motor)
* [Temperature and humidity senzor (DHT11)](https://components101.com/sensors/dht11-temperature-sensor)
* [10k ohm resistance](https://www.digchip.com/datasheets/parts/datasheet/1838/RSF100JB-10K.php)
* [Motor Driver (L239)](https://components101.com/ics/l293d-pinout-features-datasheet)
* battery 9V
* &nbsp;
* [Raspbian OS](https://www.raspberrypi.org/software/)

## Setup and Build Plan

- [x] To setup the raspberry Follow this video: https://www.youtube.com/watch?v=Hdm26W9dHK0&t=811s
- [x] Configure the elements on breadboard like in the schematics image
- [x] Test the program, write the following command on the console
      ```sudo pip3 install Adafruit_DHT```
      
      Create a new py file and add the code from the prj.py file, run it with
	  ```python3 file_name.py```

