# LESSON 7
import time

import RPi.GPIO as GPIO

delay = 0.1
in_pin = 40
out_pin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_pin, GPIO.OUT)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        read_value = GPIO.input(in_pin)
        print(read_value)
        if read_value == 1:
            GPIO.output(out_pin, 1)
            time.sleep(delay)
        if read_value == 0:
            GPIO.output(out_pin, 0)
            time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("It's been interrupted...")
