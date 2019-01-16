from socket import *
from time import ctime 
import random

HOST = '10.154.152.4'
PORT = 5002
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
msg = ['emmm', '你好阿', '世界好大吖', '我喜欢你噢', '好的', '没错呐', '你喜欢我嘛', '不行嗷', '我是机器人呢', '快点睡觉', '我能陪你聊到天亮', '你的心思我都知道噢']
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
        reply_msg = msg[random.randint(0, len(msg) - 1)]
        print('[%s] 回复: %s'%(ctime(), reply_msg))
        tcpCliSock.send(('%s' %(reply_msg)).encode())
    tcpCliSock.close()
tcpSerSock.close()
