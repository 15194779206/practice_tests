from socket import *
import time
#广播地址
dest =(('10.16.129.97',7777))
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data ="天气信息"
while True:
    time.sleep(2)
    s.sendto(data.encode(),dest)

s.close()
