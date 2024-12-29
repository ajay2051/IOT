# LESSON 42: How to Build a Simple Client Server System with Raspberry Pi

# SERVER

import socket
import time
import RPi.GPIO as GPIO
import dht11

GPIO.setmode(GPIO.BCM)

my_dht = dht11.DHT11(pin=27)

buffer_size = 1024
server_ip = "192.168.101.129"
server_port = 2222
rpi_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rpi_server.bind((server_ip, server_port))
print("Server ready...")
while True:
    cmd, address = rpi_server.recvfrom(buffer_size)
    cmd = cmd.decode('utf-8')
    print(cmd)
    print('Client address:', address[0])
    if cmd == 'GO':
        result = my_dht.read()
        if result.is_valid():
            temperature = str(result.temperature)
            humidity = str(result.humidity)
            data = temperature + " : " + humidity
            data = data.encode('utf-8')
            rpi_server.sendto(data, address)
        if not result.is_valid():
            data = 'Bad Measurement...'
            print(data)
            data=data.encode('utf-8')
            rpi_server.sendto(data, address)
    if cmd != 'GO':
        data = 'Invalid Command...'
        data=data.encode('utf-8')
        rpi_server.sendto(data, address)


# CLIENT
import socket
import time

server_address = ("192.168.101.129", 2222)
buffer_size = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cmd = 'GO'
    cmd = cmd.encode('utf-8')
    udp_client.sendto(cmd, server_address)
    data, address = udp_client.recvfrom(buffer_size)
    data = data.decode('utf-8')
    data_array = data.split(" : ")
    if len(data_array) == 1:
        print("No Data Received")
    if len(data_array) == 2:
        temperature = str(data_array[0])
        humidity = str(data_array[1])
        print("Temperature: %s Humidity: %s" % (temperature, humidity))
    time.sleep(1)