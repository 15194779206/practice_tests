import socket
'''tcp套接字客户端程序
要求：客户端中端输入不断发送消息，不输入结束运行
'''
#1：创建套接字
sockfd =socket.socket(socket.AF_INET,socket.SOCK_STREAM) #参数可不写，为默认
#2：请求连接
sockfd.connect(('10.16.129.97',7777))  #需要注意Ipv4地址不同
#3：收发消息
while True:
    message= input("comeClienMessage:")
    if not message:
        break
    sockfd.send(message.encode())
    data = sockfd.recv(1024)
    print("从服务器端接收消息",data.decode())
#4：关闭套接字
sockfd.close()
