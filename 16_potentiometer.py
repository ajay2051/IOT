# m = (y2-y1)/(x2-x1)
# (100 - 0)/(255 - 0)
# m = 100/255

# duty_cycle = (100/255)*pot_value

import time
from time import sleep

import RPi.GPIO as GPIO
import ADC0834

delay = 0.1

red_pin = 23
duty_cycle = 0
GPIO.setmode(GPIO.BCM)
ADC0834.setup(red_pin, GPIO.OUT)

my_pwm = GPIO.PWM(red_pin, 1000)
my_pwm.start(duty_cycle)

try:
    while True:
        pot_value = ADC0834.getResult(0)
        duty_cycle = (100/255) * pot_value
        if duty_cycle > 99:
            duty_cycle = 99
        my_pwm.ChangeDutyCycle(duty_cycle)
        sleep(delay)
except KeyboardInterrupt:
    my_pwm.stop()
    GPIO.cleanup()
    print("GPIO Good to Go...")