# LESSON 29 Photoresistor to detect light

import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

try:
    while True:
        light_value = ADC0834.get_results(0) # 0 is channel 0 in bread board
        print("Light value",light_value)
        time.sleep(0.2)
except KeyboardInterrupt:
    time.sleep(0.2)
    GPIO.cleanup()
    print("Bye...")