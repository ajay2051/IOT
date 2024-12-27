# LESSON 34: Create Mobile Raspberry Pi Projects with Keypad and LCD

import RPi.GPIO as GPIO
import LCD1602
import time
from KPLIB import Keypad

my_keypad = Keypad(return_char='D')
LCD1602.init(0*27, 1)

try:
    while True:
        LCD1602.write(0, 0, 'Input Value:')
        my_string = my_keypad.read_keypad()
        LCD1602.write(0, 0, 'User Input was')
        LCD1602.write(0, 1, my_string)
        time.sleep(5)
        LCD1602.clear()

except KeyboardInterrupt:
    time.sleep(0.2)
    LCD1602.clear()
    GPIO.cleanup()
