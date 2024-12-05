# LESSON 8
# When the button is pushed(DOWN) its value is 0 and when it's UP it's value is 1.
import time
import RPi.GPIO as GPIO

delay = 0.5
in_pin = 40
out_pin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_pin, GPIO.OUT)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = 0
button_state = 1
previous_button_state = 1

try:
    while True:
        button_state = GPIO.input(in_pin)
        if button_state == 1 and previous_button_state == 0:
        # if button_state == 0 and previous_button_state == 1:
            led_state = not led_state
            GPIO.output(out_pin, led_state)
        previous_button_state = button_state
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned up...")