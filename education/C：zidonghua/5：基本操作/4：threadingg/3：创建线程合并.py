from time import sleep,ctime
import threading

#创建超级播放器
def super_player(file_,time):
    for i in range(2):
        print('start playing: %s! %s' % (file_,ctime()))
        sleep(time)

#播放的文件与播放时长
lists={'爱情买卖.mp3':3,'阿凡达.mp3':5,'我和你.mp4':4}

#创建线程数组
threads=[]
#创建线程
for file_ ,time in lists.items():
    t = threading.Thread(target=super_player,args=(file_,time))
    threads.append(t)

if __name__ =='__main__':
    for t in range(len(lists)):
        threads[t].start()
    for t in range(len(lists)):
        threads[t].join()

print('all end :',ctime())

























