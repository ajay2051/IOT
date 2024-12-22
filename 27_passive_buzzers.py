# LESSON 27 Passive Buzzers

import time
import RPi.GPIO as GPIO

buzz_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_pin, GPIO.OUT)
buzzer = GPIO.PWM(buzz_pin, 400)
buzzer.start(50)
try:
    while True:
        for i in range(150, 1000):
            buzzer.ChangeFrequency(i)
            time.sleep(1/1000)
        for i in range(1000, 150, -1):
            buzzer.ChangeFrequency(i)
            time.sleep(1/1000)
        # buzzer.ChangeFrequency(100)
        # time.sleep(.1)
        # buzzer.ChangeFrequency(400)
        # time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye...")