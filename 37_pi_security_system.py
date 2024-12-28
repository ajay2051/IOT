# LESSON 37: Raspberry Pi Security System

import RPi.GPIO as GPIO
import LCD1602
import KPLIB
import time
import threading
from pygame import mixer

GPIO.setmode(GPIO.BOARD)

pir_pin = 12
GPIO.setup(pir_pin, GPIO.IN)

my_pad = KPLIB.Keypad(return_char='D')
LCD1602.init(0 * 27, 1)

my_string = ''
pwd = '1234'

mixer.init()
mixer.music.load('alarm.mp3')


def read_kp():
    global my_string
    while my_string != '*':
        my_string = my_pad.read_keypad()
        time.sleep(0.5)


read_thread = threading.Thread(target=read_kp, )
read_thread.daemon = True
read_thread.start()

while my_string != '*':
    cmd = my_string
    if cmd == 'A' + pwd:
        LCD1602.write(0, 0, 'Armed ')
        move_value = GPIO.input(pir_pin)
        if move_value == 1:
            LCD1602.write(0, 1, 'Intruder Alert...')
            mixer.music.play()
            time.sleep(10)
        if move_value == 0:
            LCD1602.write(0, 1, 'All Clear...')
    if cmd == 'B' + pwd:
        LCD1602.write(0, 0, 'UnArmed ')
        LCD1602.write(0, 1, '           ')
    if cmd == 'C' + pwd:
        LCD1602.write(0, 0, 'Change Password? ')
        LCD1602.write(0, 1, '                 ')
        while my_string == 'C' + pwd:
            pass
        pwd = my_string
        LCD1602.write(0, 0, pwd + '      ')
        time.sleep(5)
        LCD1602.write(0, 0, '      ')
        LCD1602.clear()
time.sleep(1)
LCD1602.clear()
GPIO.cleanup()
print('Bye..')
