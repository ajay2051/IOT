# LESSON 31 using keypad

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rows = [11, 13, 15, 29]
columns = [31, 33, 35, 37]

keypad = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

GPIO.setup(rows[0], GPIO.OUT)
GPIO.setup(rows[1], GPIO.OUT)
GPIO.setup(rows[2], GPIO.OUT)
GPIO.setup(rows[3], GPIO.OUT)

GPIO.setup(columns[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    my_row = int(input("Enter row number: "))
    my_column = int(input("Enter column number: "))
    while True:
        GPIO.output(rows[my_row], GPIO.HIGH)
        button_value = GPIO.input(columns[my_column])
        GPIO.output(rows[my_row], GPIO.LOW)
        if button_value == 1:
            print(keypad[my_column][my_row])
        time.sleep(0.3)
except KeyboardInterrupt:
    time.sleep(0.2)
    GPIO.cleanup()
    print("Exiting...")
