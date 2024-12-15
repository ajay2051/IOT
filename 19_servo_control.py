# LESSON 19 Servo Control

# period = 20ms
# .02 seconds
# frequency = 1 / period
# 1 / 0.02 = 50Hz
# frequency = 50

# duty_cycle == 1 - 2 % -> inclined 0 degree
# duty_cycle == 10 - 15 % -> inclined 180 degree

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 50) # 50Hz
pwm.start(0)

try:
    while True:
        pwm_percent = float(input("PWM %  "))
        pwm.ChangeDutyCycle(pwm_percent)
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO Bye...")