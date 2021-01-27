import os
import time
pid =os.fork()
if pid <0:
    print("error")
elif pid ==0:
    print("child PID",os.getpid())
    print("get parent PID",os.getppid())
else:
    print("parent PID",os.getpid())
    print("get child PID",pid)

