from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)

serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

localAddr = ("",7788)

serSocket.bind(localAddr)

serSocket.listen(5)

while True:
	print('---------主进程----------')

	newSocket,destAddr = serSocket.accept()

	print('---------主进程，接下来处理的数据【%s】---------'%str(destAddr))
	print("---------newSocket.port[%s]"%str(newSocket))

newSocket.close()
serSocket.close()


