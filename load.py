mport smbus
import Adafruit_GPIO.SPI as SPI
import time
import MAX6675.MAX6675 as MAX6675
import traceback
import logging
import sys
from flask import Flask, request

# app = Flask(__name__)

# one_bulb = 0xfe
# two_bulb - 0xfc
# three_bulb = 0xf8
# four_bulb = 0xf0
# five_bulb = 0xe0
# siren = 0xdf



CLK = 24
CS = 4
DO = 25
bus = smbus.SMBus(1)
device_address = 0x3a



def load_controll(number = 5):

    while True:
        try:
            temp_check()
            if float(number) == 1:
                bus.write_byte(device_address, 0xfe)
                print("Actual power consumption is circa 200W")

            if float(number) == 2:
                bus.write_byte(device_address, 0xfc)
                print("Actual power consumption is circa 400W")

            if float(number) == 3:
                bus.write_byte(device_address, 0xf8)
                print("Actual power consumption is circa 600W")

            if float(number) == 4:
                bus.write_byte(device_address, 0xf0)
                print("Actual power consumption is circa 800W")

            if float(number) == 5:
                bus.write_byte(device_address, 0xe0)
                print("Actual power consumption is circa 1000W")
            time.sleep(5)
        except:

def temp_check ():
    max6675 = MAX6675.MAX6675(CLK,CS,DO)
    temp = max6675.readTempC()
    print(temp)
    if temp >= 35:
        bus.write_byte(device_address, 0xff)
        print("Temperature is too high! Shutting down load... \n Temperature is higher than", temp, "Celcius degree \n")
        sys.exit(1)

load_controll()