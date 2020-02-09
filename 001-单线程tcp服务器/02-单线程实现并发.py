from socket import *
import time

serSocket = socket(AF_INET,SOCK_STREAM)

localAddr = ('',7788)
serSocket.bind(localAddr)

serSocket.setblocking(False)

serSocket.listen(100)
clientAddrlist = [] 

while True:
	try:
		newSocket,destAddr = serSocket.accept()
		print("111111111111111111111111111111")
	except:
		time.sleep(1)
		print("没有收到新的客户端！")
	else:
		print("一个新的客户端到来：%s"%str(destAddr))
		newSocket.setblocking(False)
		clientAddrlist.append((newSocket,destAddr))
		time.sleep(5)

	
	for clientSocket,clientAddr in clientAddrlist:
		try:
			recvData = clientSocket.recv(1024)
		except:
			pass
		else:
			if len(recvData)>0:
				print("%s:%s"%(str(clientAddr),recvData))
			else:
				clientSocket.close()
				clientAddrlist.remove((clientSocket,clientAddr))
				print("%s 已下线"%str(clientAddr))
