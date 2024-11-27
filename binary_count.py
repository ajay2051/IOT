import time
import RPi.GIO as GPIO


GPIO.setmode(GPIO.BOARD)

LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29

ON = 1
OFF = 0

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)

# Decimal Number 0
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(0.5)

# Decimal Number 1
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(0.5)

# Decimal Number 2
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(0.5)

GPIO.cleanup()

# TODO: Continue upto 31

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)

try:
    # Display decimal numbers from 0 to 31
    for number in range(32):
        # Convert decimal to binary and pad to 5 bits
        binary = [int(bit) for bit in format(number, '05b')]

        # Set each LED based on binary representation
        GPIO.output(LED1, binary[0])
        GPIO.output(LED2, binary[1])
        GPIO.output(LED3, binary[2])
        GPIO.output(LED4, binary[3])
        GPIO.output(LED5, binary[4])

        time.sleep(0.5)

finally:
    # Ensure GPIO is cleaned up even if an error occurs
    GPIO.cleanup()
