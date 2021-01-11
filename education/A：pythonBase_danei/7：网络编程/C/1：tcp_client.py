import socket
'''tcp套接字客户端程序'''
#1：创建套接字
sockfd =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #参数可不写，为默认
#2：请求连接
sockfd.connect(('10.16.129.97',7777))  #需要注意Ipv4地址不同
#3：收发消息
sockfd.send('我是客户端消息'.encode())
data = sockfd.recv(1024)
print("服务器端接收消息",data.decode())
#4：关闭套接字
sockfd.close()
