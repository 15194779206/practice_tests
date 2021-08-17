'''fork函数演示'''
import os
pid = os.fork()
if pid < 0:
    print("creat process failed")
elif pid == 0:
    print("the new process")
else:
    print("the old process")
print("fork test over")
