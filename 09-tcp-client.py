from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.1.6",8989))

clientSocket.send("haha".encode("gb2312"))

recvData = clientSocket.recv(1024)

print("revcData:%s"%recvData)

clientSocket.close()
