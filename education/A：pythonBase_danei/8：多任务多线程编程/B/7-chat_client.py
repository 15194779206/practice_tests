"""

"""
from socket import *
import os,sys

#服务器地址
ADDR=("0.0.0.0",8888)

def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("input your name:")
        msg = "L "+name
        s.sendto(msg.encode(), ADDR)
        #等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    #创建新的进程
    pid =os.fork()
    if pid <0:
        sys.exit("Error")
    elif pid == 0:  #子进程
        send_msg(s,name)
    else: #父进程
        recv_msg(s)

#发送消息
def send_msg(s,name):
    while True:
        try:
            text = input("发言：")
        except KeyboardInterrupt:
            text ='quit'

        if text =='quit': #输入quit表示退出聊天室
            msg ="Q"+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg ="C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

#接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        #服务端啊发送EXIT表示让客户端退出
        if data.decode() =='EXIT':
            sys.exit()
        print(data.decode()+"\n发言：",end='')

if __name__ == '__main__':
    main()