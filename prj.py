# Call it with 2 command line arguments: 'temp'/'hum' for temperature or humidity and a limit (float or int)

import Adafruit_DHT # import Adafruit
import RPi.GPIO as GPIO # import GPIO
import time # import time
import sys

DHT_SENSOR = Adafruit_DHT.DHT11 # temp and hum sensor
DHT_PIN = 4 # GPIO4 pin for data of dht11 sensor

# GPIO pins for Motor Driver Inputs
Motor1A = 24
Motor1B = 23
Motor1E = 25

TEMPERATURE = "temp"
HUMIDITY = "hum"

# setup the motor driver
def setup():
        GPIO.setmode(GPIO.BCM)  # GPIO Numbering
        GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

# cleanup the motor driver
def destroy():
        GPIO.cleanup()

# main loop
def loop(OPTION, LIMIT):
        while True:
                # read humidity and temperature from the sensor
                humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

                # check the temp and hum are valid
                if humidity is not None and temperature is not None:

                        if OPTION == TEMPERATURE:
                                if temperature >= LIMIT:
                                        turnOnMotor()
                                        print("\033[0;31;40m Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                                else:
                                        turnOffMotor()
                                        print("\033[0;32;40m Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                        elif OPTION == HUMIDITY:
                                if humidity >= LIMIT:
                                        turnOnMotor()
                                        print("\033[0;31;40m Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                                else:
                                        turnOffMotor()
                                        print("\033[0;32;40m Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                else:
                        print("\033[0;34;40m Sensor failure. Check wiring. Motor stops");
                        turnOffMotor()

                # dht11 can be checked a maximum of 1/s
                time.sleep(3);

# turn on the dc motor
def turnOnMotor():
        # Going forwards
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

# turn off the dc motor
def turnOffMotor():
        # Stop
        GPIO.output(Motor1E,GPIO.LOW)


def main():
        if len(sys.argv) != 3:
                print("Please choose temp/hum and a limit")
                return
        elif sys.argv[1] != TEMPERATURE and sys.argv[1] != HUMIDITY:
                print("Please type temp/hum")
                return

        setup()
        try:
                OPTION = sys.argv[1]
                LIMIT = float(sys.argv[2])
                loop(OPTION, LIMIT)
        except KeyboardInterrupt:
                destroy()
        except ValueError:
                print("Please type a limit")
                destroy()

main()