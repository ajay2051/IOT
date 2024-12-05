# LESSON 10

import RPi.GPIO as GPIO
import time


delay = 0.1
button_1 = 40
button_2 = 38

button_1_state = 1
button_1_state_old = 1
button_2_state = 1
button_2_state_old = 1
LED_Pin = 37
duty_cycle = 99 # If duty cycle is made 100% program can be crashed

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_Pin, GPIO.OUT)
my_pwm = GPIO.PWM(LED_Pin, 100)
my_pwm.start(duty_cycle)
button_push = 10

try:
    while True:
        button_1_state = GPIO.input(button_1)
        button_2_state = GPIO.input(button_2)
        if button_1_state_old == 0 and button_2_state_old == 1:
            button_push = button_push - 1
            duty_cycle = int(1.5849) ** button_push
            # duty_cycle = duty_cycle / 10
            print('Dim Event')
        if button_2_state_old == 0 and button_1_state_old == 1:
            button_push = button_push + 1
            duty_cycle = int(1.5849) ** button_push
            # duty_cycle = duty_cycle * 10
            print('Bright Event')
        if duty_cycle > 99:
            duty_cycle = 99
        if duty_cycle < 0:
            duty_cycle = 0
        my_pwm.ChangeDutyCycle(duty_cycle)
        button_1_state_old = button_1_state
        button_2_state_old = button_2_state
        time.sleep(delay)
except KeyboardInterrupt:
    my_pwm.stop()
    GPIO.cleanup()
