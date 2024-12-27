# LESSON 35: Monitoring User Input from Keypad Using Threading

import LCD1602
from KPLIB import Keypad
import time
import threading

my_pad = Keypad(return_char='D')

LCD1602.init(0 * 27, 1)
my_string = ''
pwd = '1234'


def read_kp():
    global my_string
    while True:
        my_string = my_pad.read_keypad()
        time.sleep(0.2)


read_thread = threading.Thread(target=read_kp, )
read_thread.daemon = True
read_thread.start()

while True:
    cmd = my_string
    if cmd == 'A' + pwd:
        LCD1602.write(0, 0, 'Armed ')
    if cmd == 'B' + pwd:
        LCD1602.write(0, 0, 'UnArmed ')
    if cmd == 'C' + pwd:
        LCD1602.write(0, 0, 'New Password? ')
        while my_string == 'C' + pwd:
            pass
        pwd = my_string
        LCD1602.write(0, 0, pwd + ' ')
        time.sleep(2)
        LCD1602.clear()
