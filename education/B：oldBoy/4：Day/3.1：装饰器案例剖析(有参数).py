import time

#装饰器=嵌套函数+高阶函数
def timer(func):    #timer(test2)   func=test2
    # 此处的args为不固定的参数，如果被装饰的函数中有参数进行调用
    def deco(*args,**kwargs):    #test2=deco
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time %s"%(stop_time-start_time))
    return  deco
"""
@timer
#test1=timer(test1)
#timer为装饰器,在被装饰函数的上面写上@函数名 实现调用
def test1():
    time.sleep(3)
    print("in the test1")
test1()
"""

@timer   #test2=timer(test2)=deco
def test2(name):
    print("输出：",name)
test2("alex")

