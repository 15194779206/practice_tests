import time

# def con(funcc):
#     print(funcc)  #打印内存地址
#     start_time=time.time()
#     funcc()
#     stop_time=time.time()
#     print("run time is %s"%(stop_time-start_time))
#
#
#
# def timmer():
#     time.sleep(3)
#     print("time ender")
#
# con(timmer)

def bar():
    time.sleep(3)
    print("in the bar")
def test2(func):
    print(func)
    return func

test2(bar)