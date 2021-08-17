"""
练习2：为两个已有功能（存款取款），添加新功能
"""
def func_dition(func):
    def wapper(*args):
        print("验证账户")
        return func(*args)
    return wapper

@func_dition
def deposit(money):
    print("存款",money)

def withdraw():
    print("取钱")
    return 10000

deposit(5000)


"""
练习3：为学生的学习方法，添加新功能（统计执行时间）
"""
import time
def sumTime(func):
    def timeall(*args):
        start_time = time.time()
        print("start",start_time)
        result =func(*args)
        end_time = time.time()
        print("end", end_time)
        print("差值：", end_time - start_time)
        return result

    return timeall

class Student:
    def __init__(self,name):
        self.name =name
    @sumTime
    def study(self):
        print("开始学习啦")
        time.sleep(2)

stu = Student("张三")
stu.study()




















