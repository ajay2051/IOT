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

import time
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BOARD)

# Define LED pins
LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29

# LED ON/OFF constants
ON = 1
OFF = 0

# Setup LED pins as output
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)

# Store LEDs in a list for easier iteration
LEDS = [LED1, LED2, LED3, LED4, LED5]

try:
    for number in range(32):  # Loop through numbers 0 to 31
        # Convert the number to binary and pad with leading zeros
        binary_representation = f"{number:05b}"

        # Set each LED state based on the binary representation
        for i, led in enumerate(LEDS):
            GPIO.output(led, ON if binary_representation[i] == '1' else OFF)

        print(f"Displaying decimal {number} as binary {binary_representation}")
        time.sleep(0.5)  # Pause for 0.5 seconds

finally:
    GPIO.cleanup()  # Cleanup GPIO settings
