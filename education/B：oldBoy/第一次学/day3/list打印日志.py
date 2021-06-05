# 引用时间函数
import  time
# 定义一个函数，多次使用
def login1():
    # 引用时间函数的固定写法
    time_f='%Y-%m-%d %X'
    time_c=time.strftime(time_f)
    with  open('a.txt','a+',encoding="utf-8") as f:
         f.write("ending %s  coding \n"%time_c)

def one():
    print("oo")
    login1()
def two():
    print("tt")
    login1()
def three():
    print("ss")
    login1()

one()
two()
three()
