# LESSON 23 Measuring Speed

# distance(d) = rate(r) * time(t)
# rate(r) = Speed of Sound
# time(t) = ping travel time

# r = d / t
# r = 16 inch / ptt in seconds

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger_pin = 23
echo_pin = 24

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

try:
    while True:
        GPIO.output(trigger_pin, 0)
        time.sleep(2E-6)
        GPIO.output(trigger_pin, 1)
        time.sleep(10E-6)
        GPIO.output(trigger_pin, 0)
        while GPIO.input(echo_pin) == 0:
            pass
        echo_start_time = time.time()
        while GPIO.input(echo_pin) == 1:
            pass
        echo_stop_time = time.time()
        ping_travel_time = echo_stop_time - echo_start_time
        speed_of_sound = 16/ping_travel_time * (3600 / (12 * 5280))
        print("speed of sound is ", speed_of_sound, "MPH")
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("......")