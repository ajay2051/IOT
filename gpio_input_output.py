# LESSON 6
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Input pin is connected to 40 and output to 1 i.e 3.3V
# If output is connected to Ground then print(read_value) will be 0

in_pin = 40
GPIO.setup(in_pin, GPIO.IN)

try:
    while True:
        read_value = GPIO.input(in_pin)
        print(read_value) # It gives 1
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
