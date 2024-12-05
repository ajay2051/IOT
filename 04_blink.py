import RPi.GPIO as GPIO
import time

cont = "Y"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while cont == "Y":
    num_blink = int(input("Enter number of blinks: "))
    if num_blink <= 0:
        num_blink = 1
    for i in range(0, num_blink):
        GPIO.output(11, True)
        time.sleep(0.5)
        GPIO.output(11, False)
        time.sleep(0.5)
    cont = input("Do you want to continue?(Y/N)")
GPIO.cleanup()
