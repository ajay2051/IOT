# LESSON 67: Controlling an RGB LED with a Capacitive Touch Sensor with Python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

touch_pin = 17
GPIO.setup(touch_pin, GPIO.IN)

button_state = 0
button_state_old = 0
index = 0

red_pin = 5
green_pin = 13
blue_pin = 19

led_pins = [red_pin, green_pin, blue_pin]

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

led_states = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

GPIO.output(led_pins, (0, 0, 0))

try:
    while True:
        button_state = GPIO.input(touch_pin)
        print("button_state=", button_state)
        time.sleep(0.5)
        if button_state == 0 and button_state_old == 1:
            print(led_states[index])
            GPIO.output(led_pins, led_states[index])
            index += 1
            if index > 4:
                index = 0
        button_state_old = button_state

except KeyboardInterrupt:
    GPIO.cleanup()
