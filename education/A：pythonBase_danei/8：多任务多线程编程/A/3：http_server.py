from socket import *

#处理浏览器的http请求
def handle(connfd):
    print("request from",connfd.getpeername())
    request = connfd.recv(4096)
    if not request:
        return
    request_line = request.splitlines()[0].decode() #获取第一行 GET / HTTP/1.1
    info=request_line.split(' ')[1] #获取/
    if info =='/':
        f=open('tests.html','r',encoding='utf-8')
        response = "Http/1.1 200 ok\r\n"
        response+="Content-Type:text/html\r\n"
        response+="\r\n"
        response+=f.read()
    else:
        response = "Http/1.1 200 ok\r\n"
        response += "Content-Type:text/html\r\n"
        response += "<h1>Sorry .....</h1>"
    #向浏览器发送内容
    connfd.send(response.encode())

#搭建tcp网络
def main():
    sockfd =socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('10.16.129.97',5555))
    sockfd.listen()
    print("listern the port 5555")
    while True:
        connfd,addr= sockfd.accept()
        handle(connfd)
        connfd.close()


if __name__ == '__main__':
    main()

#操作，火狐浏览器打开 http://10.16.129.97:5555/