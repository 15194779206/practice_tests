'''
1.创建upd套接字
2.设置套接字为可以接收广播
3.选择端口接收
'''

from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.getsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(('192.168.50.113',7777))
while True:
    try:
        msg,addr=s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    else:
        print(msg.decode())
s.close()

