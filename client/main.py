import socket
import time

#SERVER_IP = '172.18.0.2'
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5551

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

TARGET = (SERVER_IP,SERVER_PORT)

MESSAGE = "default message"


while True:
	print("enviando message")
	udp.sendto(bytes(MESSAGE,'utf-8'),TARGET)
	time.sleep(10)
udp.close()
