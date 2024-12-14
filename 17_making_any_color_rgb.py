import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)

led_red = 23
led_green = 24
led_blue = 21


GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)


my_pwm_red = GPIO.PWM(led_red, 1000)
my_pwm_green = GPIO.PWM(led_green, 1000)
my_pwm_blue = GPIO.PWM(led_blue, 1000)

my_pwm_red.start(0)
my_pwm_green.start(0)
my_pwm_blue.start(0)

ADC0834.setup()
try:
    while True:
        analog_red = ADC0834.getResult(0)
        analog_green = ADC0834.getResult(0)
        analog_blue = ADC0834.getResult(0)

        print('RawRed= ', analog_red, 'Vol= ', analog_red / 255 * 5)
        dc_red = analog_red * 100 / 255
        if dc_red <=3:
            dc_red = 0
        my_pwm_red.ChangeDutyCycle(dc_red)
        time.sleep(.2)

        print('RawGreen= ', analog_green, 'Vol= ', analog_green / 255 * 5)
        dc_green = analog_green * 100 / 255
        if dc_green <=3:
            dc_green = 0
        my_pwm_green.ChangeDutyCycle(dc_green)
        time.sleep(.2)

        print('RawBlue= ', analog_blue, 'Vol= ', analog_blue / 255 * 5)
        dc_blue = analog_blue * 100 / 255
        if dc_blue <=3:
            dc_blue = 0
        my_pwm_blue.ChangeDutyCycle(dc_blue)
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')