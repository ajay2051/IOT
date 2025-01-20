# LESSON 69: Controlling an RGB LED with RFID Tags and Modules

import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

reader = SimpleMFRC522()

red_pin = 16
green_pin = 20
blue_pin = 21

color_pins = [red_pin, green_pin, blue_pin]
colors = {
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
}
GPIO.setup(color_pins, GPIO.OUT)

try:
    while True:
        print("Place Card Next to Reader...")
        id, text = reader.read()
        text = text.strip()
        print("ID:", id, "TEXT:", text)
        print("Remove your card...")
        time.sleep(1)
        if text == 'ADMIN':
            name = input("Enter New Person Name: ")
            color = (input("Enter New Person Color: "))
            print(name, color)
            data_str = name + ", " + color
            print(data_str)
            reader.write(data_str)
            print("Place Remove Card Next to Reader...")
            time.sleep(1)
        if text != 'ADMIN':
            print(text)
            data_array = text.split(',')
            name = data_array[0]
            color = data_array[1].lower()
            print(name, color)
            data_str = name + ", " + color
            print(data_str)
            GPIO.output(color_pins, colors[color])
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting...")
