# LESSON 41: How to Send Data to the PC over WiFi or Ethernet Using UDP
# SERVER

import socket
import time

buffer_size = 1024
msg_from_server = "Client..."
server_port = 2222
server_ip = "192.168.101.129"
bytes_to_send = msg_from_server.encode('utf-8')

rpi_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rpi_socket.bind((server_ip, server_port))
print("Server ready...")
counter=0
while True:
    message, address = rpi_socket.recvfrom(buffer_size)
    message = message.decode('utf-8')
    print("Message ", message)
    if message == "INC":
        counter += 1
    if message == "DEC":
        counter -= 1
    message = str(counter)
    message = message.encode('utf-8')
    rpi_socket.sendto(message, address)

# CLIENT

import socket

msg_from_client = "Howdy Server..."
bytes_to_send = msg_from_client.encode('utf-8')
server_address = ('192.168.101.129', 2222)
buffer_size = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cmd = input("What would you like to send?, INC or DEC?: ")
    cmd = cmd.encode('utf-8')
    udp_client.sendto(cmd, server_address)
    data, address = udp_client.recvfrom(buffer_size)
    data = data.decode('utf-8')
    print("Data", data)
    print("Server IP Address", address[0])
    print("Server Port", address[1])
