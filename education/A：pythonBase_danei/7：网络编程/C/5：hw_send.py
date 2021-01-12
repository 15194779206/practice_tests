from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.connect(('10.16.129.97',6666))
f=open('picture.png','rb')

while True:
    data = f.read(1024)
    sockfd.send(data)

f.close()
sockfd.close()
