# LESSON 30 Alarm for Detecting Motion in the Dark

import ADC0834
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motion_pin = 23
buzz_pin = 26

GPIO.setup(buzz_pin, GPIO.OUT)
GPIO.output(buzz_pin, GPIO.HIGH)

GPIO.setup(motion_pin, GPIO.IN)
ADC0834.setup()
time.sleep(2)

try:
    while True:
        motion = GPIO.input(motion_pin)
        light_value = ADC0834.get_results(0)
        print("light Value", light_value, "Motion", motion)
        time.sleep(0.5)
        if motion ==1 and light_value <= 140:
            GPIO.output(buzz_pin, GPIO.LOW)
            print("Intruder")
        else:
            print("All Clear")
            GPIO.output(buzz_pin, GPIO.HIGH)
except KeyboardInterrupt:
    time.sleep(0.2)
    GPIO.cleanup()
    print("Bye...")