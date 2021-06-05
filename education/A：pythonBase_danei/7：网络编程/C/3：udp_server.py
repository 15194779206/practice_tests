'''UPD套接字服务端'''
from socket import *
#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
#绑定地址
sockfd.bind(('10.16.129.97',7777))
#收发消息
while True:
    data,addr =sockfd.recvfrom(1024)
    print("接收到的消息",data.decode())
    sockfd.sendto("server_say".encode(),addr)
#关闭套接字
sockfd.close()