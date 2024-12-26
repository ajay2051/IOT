# LESSON 33 Creating a Python Class and Library for Reading a Keypad

import RPi.GPIO as GPIO
import time

class Keypad:
    def __init__(self, rows=[11, 13, 15, 29], columns=[31, 33, 35, 37],
                 key_labels=[['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']], return_char='D'):
        self.rows = rows
        self.columns = columns
        self.key_labels = key_labels
        self.return_char = return_char

        GPIO.setmode(GPIO.BOARD)

        for i in rows:
            GPIO.setup(i, GPIO.OUT)

        for j in columns:
            GPIO.setup(j, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def read_keypad(self):
        key_strokes = ''
        no_press = True
        no_press_old = True
        while True:
            no_press = True
            for my_row in [0,1,2,3]:
                for my_col in [0,1,2,3]:
                    GPIO.output(self.rows[my_row], GPIO.HIGH)
                    button_value = input(self.columns[my_col])
                    GPIO.output(self.rows[my_row], GPIO.LOW)
                    if button_value == 1:
                        my_char = self.key_labels[my_row][my_col]
                        if my_char == self.return_char:
                            return key_strokes
                        no_press = False
                    if button_value == 1 and no_press_old == True and no_press == False:
                        key_strokes = key_strokes + self.key_labels[my_row][my_col]
            no_press_old = no_press
            time.sleep(0.2)


my_pad = Keypad()
my_string = my_pad.read_keypad()
print(my_string)
GPIO.cleanup()