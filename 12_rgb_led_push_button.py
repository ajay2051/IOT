# LESSON 12

# RGB LED PUSH BUTTON

import time

import RPi.GPIO as GPIO



red_pin = 37
green_pin = 35
blue_pin = 33

red_button = 11
green_button = 13
blue_button = 15

red_button_state = 1
red_button_state_old = 1

green_button_state = 1
green_button_state_old = 1

blue_button_state = 1
blue_button_state_old = 1

red_led_state = 0
green_led_state = 0
blue_led_state = 0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

GPIO.setup(red_button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(blue_button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# GPIO.output(red_pin, 0)

try:
    red_button_state = GPIO.input(red_button)
    green_button_state = GPIO.input(green_button)
    blue_button_state = GPIO.input(blue_button)
    print("Button States...", red_button_state, green_button_state, blue_button_state)
    if red_button_state == 1 and red_button_state_old == 0:
        print("Red Channels Registered...")
        red_led_state = not red_led_state
        GPIO.output(red_pin, red_led_state)

    if green_button_state == 1 and green_button_state_old == 0:
        print("Green Channels Registered...")
        green_led_state = not green_led_state
        GPIO.output(green_pin, green_led_state)

    if blue_button_state == 1 and blue_button_state_old == 0:
        print("Blue Channels Registered...")
        blue_led_state = not blue_led_state
        GPIO.output(blue_pin, blue_led_state)

    red_button_state_old = red_button_state
    green_button_state_old = green_button_state
    blue_button_state_old = blue_button_state
    time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Shutting Down...")