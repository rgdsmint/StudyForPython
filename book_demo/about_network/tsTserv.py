from socket import *
from time import ctime 

HOST = '192.168.1.2'
PORT = 5002
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connected...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)


    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        strData = data
        print('[%s] %s: %s' %(ctime(), '收到', strData))
        reply = input('[%s] 回复:'%(ctime()))
        tcpCliSock.send(('%s' %(reply)).encode())
    tcpCliSock.close()
tcpSerSock.close()