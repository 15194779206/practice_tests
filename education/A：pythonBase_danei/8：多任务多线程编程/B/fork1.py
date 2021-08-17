import os
import time
print("======================")
a=1

pid = os.fork()
if pid < 0:
    print("error")
elif pid ==0:
    print("child process")
    print("a=%s"%a)
    a=10000
else:
    time.sleep(1)
    print("Parent process")
    print(a)

print("all:",a)