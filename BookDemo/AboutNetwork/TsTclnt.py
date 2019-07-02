
from socket import *
from time import ctime
HOST = '10.154.152.4'
PORT = 5002
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('[%s] 发送:'%(ctime()))
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print('[%s] 收到: %s'%(ctime(), data))
tcpCliSock.close()

