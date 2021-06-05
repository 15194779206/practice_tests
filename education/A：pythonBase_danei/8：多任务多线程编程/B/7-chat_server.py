"""
chat room
"""
from socket import *
import os,sys

ADDR=('0.0.0.0',8888)

#存储用户信息
user={}


#创建网络连接
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid =os.fork()
    if pid <0:
        return
    elif pid ==0: #发送管理员消息
        while True:
            msg = input("管理员消息：")
            msg ="C 管理员消息 "+msg
            s.sendto(msg.encode(),ADDR)
    else:
        #请求处理
        do_request(s)

def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        msg = data.decode().split(' ')
        if msg[0] == 'L':  #进入聊天室
            do_login(s, msg[1],addr)
        elif msg[0] == 'C': #聊天
            text =' '.join(msg[2:]) #以防发送的信息中包含空格，所以进行拼接
            do_chat(s,msg[1],text)
        elif msg[0] == 'Q':  #退出聊天室
            if msg[1] not in user:  #可能存在服务端重新启动，客户端不知道，循环遍历user表
                s.sendto(b'EXIT',addr)
                continue
            do_quit(s,msg[1])


def do_login(s,name,addr):
    print(user)
    if name in user or "管理员" in name:
        s.sendto("\n该用户已存在".encode(),addr)
        return
    s.sendto(b'OK', addr)
    #通知其他人
    msg = "\n欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(), user[i])
    #将用户加入
    user[name] =addr

def do_chat(s,name,text):
    msg ="%s : %s"%(name,text)
    for i in user:
        if i!=name:
            s.sendto(msg.encode(),user[i])

#退出
def do_quit(s,name):
    msg ="%s退出聊天室"%name
    for i in user:
        if i!=name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    #将用户删除
    del user[name]

if __name__ == '__main__':
    main()






























