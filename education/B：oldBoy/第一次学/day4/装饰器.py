import time

# 装饰器=高阶函数+嵌套函数
def timer1(func):
    # 如果被装饰的函数有参数，在装饰器中添加上参数，因不确定参数的个数，添加上参数组
    def test3(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("time %s"%(stop_time-start_time))
    return  test3
# test1=timmer(test1)   #调用装饰器，不改变被装饰函数的调用方式
@timer1  #在被装饰函数的上面写上@函数名 实现调用
def test1():
    time.sleep(3)
    print("in the test1")
test1()

# test2中含有参数，进行运行
@timer1
def test2(name,age):
    print("name",name,age)

# test2=timmer(test2)
test2("alex",22)