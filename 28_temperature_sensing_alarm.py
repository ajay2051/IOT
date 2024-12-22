# LESSON 28 Temperature Sensing Alarm

import RPi.GPIO as GPIO
import time
import ADC0834
import LCD1602
import dht11

GPIO.setmode(GPIO.BCM)

buzz_pin = 26
temp_pin = 26
button_pin = 24

my_dht = dht11.DHT11(pin=temp_pin)
GPIO.setup(buzz_pin, GPIO.OUT)
GPIO.output(buzz_pin, GPIO.HIGH)

ADC0834.setup()
LCD1602.init(0 * 27, 1)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_state = 1
button_state_old = 1
set_mode = True
buzz_value = 85

try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == 1 and button_state_old == 0:
            set_mode = not set_mode
        print(set_mode)
        button_state_old = button_state
        time.sleep(0.2)
        if set_mode:
            analog_value = ADC0834.get_result()
            buzz_value = int(analog_value * (100 / 255))
            LCD1602.write(0, 0, 'Set Trip Temp:')
            LCD1602.write(0, 1, str(buzz_value))
            time.sleep(0.2)
            LCD1602.clear()
            GPIO.output(buzz_pin, GPIO.HIGH)
        if not set_mode:
            result = my_dht.read()
            if result.is_valid():
                temperature_celcius = result.temperature
                temperature_fahrenheit = temperature_celcius * 9 / 5 + 32
                temperature_fahrenheit = round(temperature_fahrenheit, 2)
                print('Temperature Fahrenheit:', temperature_fahrenheit)
                print('Temperature Celcius:', temperature_celcius)
                print(buzz_value)
                humidity = result.humidity
                if temperature_fahrenheit < buzz_value:
                    GPIO.output(buzz_pin, GPIO.HIGH)
                    LCD1602.write(0, 0, 'Temp: ')
                    LCD1602.write(6, 0, str(temperature_fahrenheit))
                    LCD1602.write(11, 0, 'F')
                    LCD1602.write(0, 1, 'Humidity: ')
                    LCD1602.write(10, 1, str(humidity))
                if temperature_fahrenheit >= buzz_value:
                    GPIO.output(buzz_pin, GPIO.LOW)
                    LCD1602.write(0, 0, 'Temp: ')
                    LCD1602.write(6, 0, str(temperature_fahrenheit))
                    LCD1602.write(11, 0, 'F')
                    LCD1602.write(0, 1, 'ALERT: High Temp!')
                    # LCD1602.write(10, 1, str(humidity))
        time.sleep(0.1)
except KeyboardInterrupt:
    time.sleep(0.1)
    GPIO.cleanup()
    LCD1602.clear()
    print("Bye...")
