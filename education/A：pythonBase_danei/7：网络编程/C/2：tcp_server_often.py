import socket
'''tcp套接字服务端程序
    不断发送消息，进行收发
'''
#1：创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2：绑定地址
sockfd.bind(('10.16.129.97',7777))
#3：设置监听
sockfd.listen(5)
while True:
    print("Waiting for connect.....")
    #4：等待处理客户端连接请求
    # try:
    #     connfd,addr = sockfd.accept()
    #     print("connect from:",addr)
    # except KeyboardInterrupt:
    #     print("退出服务")
    #     break
    #5：消息收发
    while True:
        connfd, addr = sockfd.accept()
        print("connect from:",addr)
        data = connfd.recv(1024) #接收消息
        if not data:
            break
        print("接收到的消息：", data.decode())
        n=connfd.send("我是服务端，我收到消息了".encode()) #发送 n=connfd.send(b'receive message')
        print('发送%d个字节数据'%n)
    connfd.close()
    #6：关闭套接字
    sockfd.close()
