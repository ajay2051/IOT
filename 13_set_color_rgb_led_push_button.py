# LESSON 13

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

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

my_pwm_red = GPIO.PWM(red_pin, 100)
my_pwm_green = GPIO.PWM(green_pin, 100)
my_pwm_blue = GPIO.PWM(blue_pin, 100)

duty_cycle_red = 0.99
duty_cycle_green = 0.99
duty_cycle_blue = 0.99

my_pwm_red.start(int(duty_cycle_red))
my_pwm_green.start(int(duty_cycle_green))
my_pwm_blue.start(int(duty_cycle_red))

try:
    while True:
        red_button_state = GPIO.input(red_button)
        green_button_state = GPIO.input(green_button)
        blue_button_state = GPIO.input(blue_button)
        print("Button state", red_button_state, green_button_state, blue_button_state)

        if red_button_state == 1 and red_button_state_old == 1:
            duty_cycle_red = duty_cycle_red * 1.58
            print("Red Channel Registered")
            if duty_cycle_red > 99:
                duty_cycle_red = 0.99
            my_pwm_red.ChangeDutyCycle(int(duty_cycle_red))

        if green_button_state == 1 and green_button_state_old == 1:
            duty_cycle_green = duty_cycle_green * 1.58
            print("Green Channel Registered")
            if duty_cycle_green > 99:
                duty_cycle_green = 0.99
            my_pwm_green.ChangeDutyCycle(int(duty_cycle_green))

        if blue_button_state == 1 and blue_button_state_old == 1:
            duty_cycle_blue = duty_cycle_blue * 1.58
            print("Blue Channel Registered")
            if duty_cycle_blue > 99:
                duty_cycle_blue = 0.99
            my_pwm_blue.ChangeDutyCycle(int(duty_cycle_blue))

        red_button_state_old = red_button_state
        green_button_state_old = green_button_state
        blue_button_state_old = blue_button_state
        print(duty_cycle_red, duty_cycle_green, duty_cycle_blue)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print("Good to go...")