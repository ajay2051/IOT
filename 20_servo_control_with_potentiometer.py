# Lesson 20 Control servo with potentiometer

# input = 0, output = 2
# input = 255, output = 12
# In output 12 it rotates 180 degree

# slope = (y2 - y1)/(x2 - x1)
# m = (12 - 2) /(255 - 0)

# y - y1 = m(x - x1)
# y - 2 = 10/255(x - 0)
# y is pwm value and x in analog value obtained from potentiometer

import time
import RPi.GPIO as GPIO
import ADCO834

GPIO.setmode(GPIO.BCM)

pwm_pin = 4

GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(0)
ADCO834.setup()

try:
    while True:
        analog_value = ADCO834.get_results(0)
        pwm_percentage = 10/255 * ((analog_value) + 2)
        print("PWM percentage: " + str(pwm_percentage))
        pwm.ChangeDutyCycle(pwm_percentage)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleanup...")