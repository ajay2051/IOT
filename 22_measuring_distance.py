# LESSON 22 Measuring Distance

# distance(d) = rate(r) * time (t)
# rate = 767 miles / hour

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
        print("Echo time: ", echo_start_time)
        while GPIO.input(echo_pin) == 1:
            pass
        echo_end_time = time.time()
        print("Echo time: ", echo_end_time)
        ping_travel_time = echo_end_time - echo_start_time
        distance = 767*ping_travel_time*5280*12/3600
        print("Distance: ", distance, 2, "inches")
        distance_to_target = distance / 2
        print("Distance to target: ", distance_to_target)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning up...")
