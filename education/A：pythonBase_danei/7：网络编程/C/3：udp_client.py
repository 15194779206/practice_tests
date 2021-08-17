'''udp客户端套接字'''
from socket import *
#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("client_message:")
    sockfd.sendto(data.encode(),('10.16.129.97',7777))
    msg,addr = sockfd.recvfrom(1024)
    print("from server:",msg.decode())
sockfd.close()
