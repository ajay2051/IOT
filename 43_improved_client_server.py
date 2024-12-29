# LESSON 43: Building an Improved Client Server Connection to the Pi

# SERVER

import socket
import time
import dht11
import RPi.GPIO as GPIO

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
    print("Received: " + cmd)
    if cmd == 'TEMP':
        result = my_dht.read()
        while not result.is_valid():
            print("sensor reading error.")
            result = my_dht.read()
        data = cmd + ':' + str(result.temperature)
        data = data.encode('utf-8')
        rpi_server.sendto(data, address)
    if cmd == 'HUM':
        result = my_dht.read()
        while not result.is_valid():
            print("sensor reading error.")
            result = my_dht.read()
        data = cmd + ':' + str(result.humidity)
        data = data.encode('utf-8')
        rpi_server.sendto(data, address)
    if cmd != 'HUM' and cmd != 'TEMP':
        data = cmd + ':' + "null"
        data = data.encode('utf-8')
        rpi_server.sendto(data, address)


# CLIENT

import socket
import time
server_address = ('192.168.101.129', 2222)
buffer_size = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cmd = input("Enter command (TEMP, HUM)?: ")
    cmd = cmd.encode('utf-8')
    udp_client.sendto(cmd, server_address)
    data, address = udp_client.recvfrom(buffer_size)
    data = data.decode('utf-8')
    data_array = data.split(':')
    if data_array[0] == 'TEMP':
        print("Temperature: " + str(data_array[1]))
    if data_array[0] == 'HUM':
        print("Humidity: " + str(data_array[1]))
    if data_array[0] != 'TEMP' and data_array[0] != 'HUM':
        print("Invalid command.", data_array[1])
    time.sleep(0.5)
