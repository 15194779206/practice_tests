'''
1.使用tcp服务和客户端编程，将一个文件从客户端发送到服务端，文件类型为图片或者普通文本皆可
2.重点代码必须自己能写
'''
from socket import *

sockfd= socket(AF_INET,SOCK_STREAM)
sockfd.bind(('10.16.129.97',6666))
sockfd.listen(2)
connfd,addr=sockfd.accept()
f = open('copys.png','wb')
while True:
    data = connfd.recv(1024)
    f.write(data)
    connfd.send("server已经接收到消息".encode())

sockfd.close()
connfd.close()
f.close()