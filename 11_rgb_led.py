# LESSON 11

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

red_pin = 37
green_pin = 35
blue_pin = 33

try:
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)

    GPIO.output(red_pin, GPIO.HIGH)
    GPIO.output(red_pin, GPIO.LOW)

    GPIO.output(green_pin, GPIO.HIGH)
    GPIO.output(green_pin, GPIO.LOW)

    GPIO.output(blue_pin, GPIO.HIGH)
    GPIO.output(blue_pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
