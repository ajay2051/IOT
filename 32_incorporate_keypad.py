# LESSON 32 incorporate keypad

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rows = [11, 13, 15, 29]
columns = [31, 33, 35, 37]

key_pad = [
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

no_press = True
no_press_old = True

try:
    while True:
        no_press = True
        for my_row in [0, 1, 2, 3]:
            for my_col in [0, 1, 2, 3]:
                GPIO.output(rows[my_row], GPIO.HIGH)
                button_value = GPIO.input(columns[my_col])
                GPIO.output(rows[my_row], GPIO.LOW)
                if button_value == 1:
                    my_char = key_pad[my_row][my_col]
                    no_press = False
                if button_value == 1 and no_press == False and no_press_old == True:
                    print(key_pad[my_row][my_col])
            no_press_old = no_press
            time.sleep(0.2)

except KeyboardInterrupt:
    time.sleep(0.2)
    GPIO.cleanup()
    print("Exiting...")