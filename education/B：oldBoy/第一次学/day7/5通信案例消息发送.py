#客户端
import socket
client= socket.socket() #声明socket类型，同时生成socket链接对象
#绑定要监听的端口，只接受一个参数，所以写成元组
client.connect(('localhost',6969))
#注意bytes只能接受ascll码类型的数据
# client.send(b"Hello Word") #发送内容,b为转换为bytes类型
client.send("我要试试中文，需要添加encode".encode("utf-8"))
data=client.recv(1024) #接收的内容字节
# print("recv:",data)
print("recv:",data.decode())
client.close()
