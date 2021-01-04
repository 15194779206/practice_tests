import time

#装饰器
def timer(func):  #func=test1()
    def deco():
        start_time=time.time()
        func()
        close_time=time.time()
        print("haoshi is %s"%(close_time-start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print("this is test1")

test1()