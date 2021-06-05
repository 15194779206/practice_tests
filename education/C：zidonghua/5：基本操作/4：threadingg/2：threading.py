from time import sleep,ctime
from threading import Thread


def music(func,loop):
    for i in range(loop):
        print('i was listening to %s! %s' % (func,ctime()))
        sleep(2)

def move(func,loop):
    for i in range(loop):
        print('i was listening to %s! %s' % (func,ctime()))
        sleep(5)
#创建线程数组
threads=[]
#创建线程t1,并添加到线程数组
t1 = Thread(target=music,args=('爱情买卖',2)) #已经创建好的线程
threads.append(t1)#追加到线程数组

t2 = Thread(target=move,args=('阿凡达',2))
threads.append(t2)

if __name__ =='__main__':
    for t in threads: #启动线程
        t.start()
    for t in threads:#守护线程
        t.join()

print('all end :',ctime())

























