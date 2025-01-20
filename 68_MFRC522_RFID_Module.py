# LESSON 68 Using the MFRC522 RFID Module and Tag on Raspberry Pi

import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

try:
    while True:
        cmd = input("Do you want to Read or Write (R/W)...? ")
        if cmd == "W":
            txt = input("Input Your Text...")
            reader.write(txt)
        if cmd == "R":
            print("Place card on reader...")
            id, text = reader.read()
            print("id:", id, "text:", text)
            time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Bye")