# LESSON 70: Using an IR Proximity Sensor for Collision Avoidance

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

prox_pin = 17
GPIO.setup(prox_pin, GPIO.OUT, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        prox_state = GPIO.input(prox_pin)
        print("Proximity state: " + str(prox_state))
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done..")
