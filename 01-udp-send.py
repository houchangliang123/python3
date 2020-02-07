from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))

udpSocket.sendto(b"haha",("192.168.1.100",8081))
