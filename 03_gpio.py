import RPi.GPIO as GPIO
import time

ON = True
OFF = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
# GPIO.cleanup()
GPIO.output(11, ON)  # Turn On LED
GPIO.output(11, OFF)  # Turn Off LED
time.sleep(1)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, ON)
