# LESSON 24 PIR (Passive Infrared) Motion Sensor

import RPi.GPIO as GPIO
import time

motion_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motion_pin, GPIO.IN)

time.sleep(10)

try:
    while True:
        motion = GPIO.input(motion_pin)
        print(motion)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("....")
