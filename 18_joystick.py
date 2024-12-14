# LESSON 18 JOYSTICK

import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

button_pin = 21
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        analog_value_x = ADC0834.get_result(0)
        time.sleep(0.2)
        analog_value_y = ADC0834.get_result(1)
        button_state = GPIO.input(button_pin)
        print('X Value:', analog_value_x)
        print('Y Value:', analog_value_y)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye...")