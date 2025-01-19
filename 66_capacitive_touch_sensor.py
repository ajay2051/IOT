# LESSON 66: Using a Capacitive Touch Sensor with Python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
touch_pin = 17
GPIO.setup(touch_pin, GPIO.IN)

while True:
    sensor_state = GPIO.input(touch_pin)
    print(sensor_state)
    time.sleep(1)