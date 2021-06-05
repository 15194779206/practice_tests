from socket import *

s= socket(AF_INET,SOCK_STREAM)
s.bind(('10.16.129.97',5555))
s.listen()
f,addr = s.accept()
data = '''
Content-Type:text/html
<h1>ok</h1>
'''
tests= f.recv(1024)
print(tests.decode())
f.send(data.encode())
s.close()
f.close()