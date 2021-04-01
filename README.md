# Fan controlled by temperature

## Overview

The project consists of a fan attached to a DC motor. 
The temperature and humidity senzor will send data to the program.
The program can be called with 2 command line arguments representing the option (temperature or humidity) and the limit.
This motor will start spinning when the temperature or humidity is higher than the limit imposed by the user.

## Gif demo

![gif_demo](https://github.com/at-cs-ubbcluj-ro/solo-project-dogoPaprika/blob/master/media/ezgif.com-gif-maker.gif)

## Schematics plan

![fritzing_schema](https://github.com/at-cs-ubbcluj-ro/solo-project-dogoPaprika/blob/master/media/fritzing_schema.png)

## Pre-requisites

* Raspberry Pi Zero W
* Jumping wires
* DC motor
* Temperature and humidity senzor (DHT11)
* 10k ohm resistance
* Motor Driver (L239)
* battery 

## Setup and Build Plan

- [x] To setup the raspberry Follow this video: https://www.youtube.com/watch?v=Hdm26W9dHK0&t=811s
- [x] Configure the elements on breadboard like in the schematics image
- [x] Test the program
      Write the following command on the console
      ```sudo pip3 install Adafruit_DHT```
      
      Create a new py file and add the code from the prj.py file

