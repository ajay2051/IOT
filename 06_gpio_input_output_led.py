# Lesson 6 Homework
# Glow LED after push button

import RPi.GPIO as GPIO

in_pin = 40
out_pin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)

try:
    while True:
        read_value = GPIO.input(in_pin)
        if read_value == 1:
            GPIO.output(out_pin, 1)
        if read_value == 0:
            GPIO.output(out_pin, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("It's been interrupted...")
