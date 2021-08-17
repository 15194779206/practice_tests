import socket
'''tcp套接字服务端程序'''
#1：创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2：绑定地址
sockfd.bind(('10.16.129.97',7777))
#3：设置监听
sockfd.listen(5)
print("Waiting for connect.....")
#4：等待处理客户端连接请求
connfd,addr = sockfd.accept()
#5：消息收发
data = connfd.recv(1024) #接收消息
print("接收到的消息：",data.decode())
n=connfd.send("我是服务端，我收到消息了".encode()) #发送 n=connfd.send(b'receive message')
print('发送%d个字节数据'%n)
#6：关闭套接字
sockfd.close()
connfd.close()