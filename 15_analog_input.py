import RPi.GPIO as GPIO
import 15_ADCO834
import time

GPIO.setmode(GPIO.BCM)
ADCO834.setup()

try:
    while True:
         analog_value = ADCO834.getResult(0)
         # analog_value = ADCO834.getResult(0)
         print(analog_value)
         time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Good To Go...")