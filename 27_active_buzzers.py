# LESSON 27 Active Passive Buzzers

import time
import RPi.GPIO as GPIO

buzz_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(buzz_pin, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(buzz_pin, GPIO.LOW)
        time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye...")