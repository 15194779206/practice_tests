from time import sleep,ctime
#grid启动

def music():
    print('i was listening to music! %s'%ctime())
    sleep(2)

def move():
    print('i was at the movies! %s'%ctime())
    sleep(5)

if __name__ =='__main__':
    music()
    move()

print('all end :',ctime())

























