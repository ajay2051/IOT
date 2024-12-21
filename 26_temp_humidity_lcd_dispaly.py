# LESSON 26 Temperature and Humidity display in LCD

import RPi.GPIO as GPIO
import time
import LCD1602
import dht11

GPIO.setmode(GPIO.BCM)

my_dht = dht11.DHT11(pin=17)

LCD1602.init(0*27, 1)

button_pin = 21

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_state = 1
button_state_old = 1
temperature_mode = 1

try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state==1 and button_state_old==0:
            temperature_mode = not temperature_mode
        print(temperature_mode)
        button_state_old = button_state
        result = my_dht.read()
        temperature_celcius = result.temperature
        temperature_fahrenheit = temperature_celcius * 9 / 5 + 32
        humidity = result.humidity
        if result.is_valid():
            if temperature_mode == 1:
                LCD1602.write(0,0 , "Temp: ")
                LCD1602.write(6, 0, str(temperature_fahrenheit))
                LCD1602.write(10,0 , "Humidity: ")
                LCD1602.write(16,0, str(humidity))
            if temperature_mode == 0:
                LCD1602.write(0,0 , "Temp: ")
                LCD1602.write(6, 0, str(temperature_celcius))
                LCD1602.write(10,0 , "Humidity: ")
                LCD1602.write(16,0, str(humidity))

except KeyboardInterrupt:
    time.sleep(0.5)
    GPIO.cleanup()
    LCD1602.cleanup()
    print("Bye...")