# LESSON 25 Measure Temperature and Humidity with the DHT-11 Sensor
# pip install dht11

import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin = 17)

try:
    while True:
        result = instance.read()

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            time.sleep(0.2)
        else:
            print("Error: %d" % result.error_code)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("...")
