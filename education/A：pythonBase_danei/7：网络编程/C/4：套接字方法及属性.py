from socket import *



#属性详解
s=socket()
s.bind(('10.16.129.97',7777))
# s.listen(3)
# c,addr = s.accept()

print("地址类型",s.family) #AddressFamily.AF_INET
print("套接字类型",s.type) #SocketKind.SOCK_STREAM
print("获取套接字绑定地址",s.getsockname()) #('10.16.129.97', 7777)
print("描述符",s.fileno())
# print("获取客户端地址",c.getpeername())  #必须和客户端进行连接才能操作
s.setsockopt(SOL_SOCKET,)
