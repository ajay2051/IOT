# LESSON 9
# GPIO Pins for PWM to Simulate Analog Output (Pulse Width Modulation)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, True)
GPIO.output(37, False)

my_pwm = GPIO.PWM(37, 100)
my_pwm.start(50)
my_pwm.stop(50)
my_pwm.ChangeDutyCycle(75) # Not 0 and 100
my_pwm.ChangeFrequency(50)
my_pwm.stop()
GPIO.cleanup()