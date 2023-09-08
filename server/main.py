#!/usr/bin/python3
#servidor_UDP.py

import socket

MY_IP='' #  essa configuração possibilita escutar em várias interfaces
MY_PORT=5551

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MY_SERVER = (MY_IP,MY_PORT)

udp.bind(MY_SERVER)

RECEIVED_MESSAGE,CLIENT_ADDRESS = udp.recvfrom(1024) # must be 2 multiple

print(f"Received: {RECEIVED_MESSAGE} - Client : {CLIENT_ADDRESS}")

udp.close()
