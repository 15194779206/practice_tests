import socket

server=socket.socket()
server.bind(('localhost',6969)) #绑定要监听端口
server.listen() #监听
print("我要开始等电话了")
conn,addr=server.accept() #等电话打进来
#conn就是客户端连过来而在服务器端为其生成的一个连接实例
#conn用来接收和发送数据。address是连接客户端的地址。
print(conn,addr)
print("电话来了")
data=conn.recv(1024)  #接受数据
print("recv:",data.decode())
conn.send(data.upper()) #数据转回发送给客户端
server.close()


