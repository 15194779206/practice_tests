import os
from time import sleep
pid =os.fork()

if pid<0:
    print("error")
elif pid ==0:
    print("child pid",os.getpid())
    print("parent pid1", os.getppid())
    os._exit(2)
else:
    pid,status = os.waitpid(-1,os.WNOHANG)
    print("pid:",pid)  #退出的子进程PID
    print("status",status) #子进程退出状态
    print("parent pid",os.getpid())

print("over pid")