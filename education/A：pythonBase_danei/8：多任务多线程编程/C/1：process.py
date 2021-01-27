#multiprocessing示例
import multiprocessing as mp
import time
a=1

#子进程函数
def fun():
    print("子进程开始执行")
    global a
    print("a=",a)
    a=10000
    time.sleep(3)
    print('a2=',a)
    print("子进程结束执行")

#创建进程对象
p=mp.Process(target=fun)

#启动进程
p.start()

time.sleep(2)
print("父进程")
print("a1=",a)

#回收进程
p.join()