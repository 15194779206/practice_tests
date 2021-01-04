#从学生视图解析这个问题
import os
import sys

# 导入路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education
#注册
def login(func):
    def inner():
        _uername="alex"
        _password="admin"
        global user_status

        if user_status==False:
            username=input("user:")
            password=input("password:")
            if username==_uername and password==_password:
                print("welcome...")
                user_status=True
            else:
                print("用户名或密码错误")
        if user_status==True:
            func()
    return inner

def add_student():
    Stu_name=input("请输入姓名：")


def pay_tuition():
    pass
def choose_grade():
    pass
def choose_school():
    pass

def run():
    print("学生视图：")
    print("=" * 20)
    while True:
        print("1.注册\n2.交学费\n3.选择班级\n4.选择学校\n")
        res = input("输入序号：")
        if res == "1":
            add_student()
        elif res == "2":
            pay_tuition()
        elif res == "3":
            choose_grade()
        elif res == "4":
            choose_school()
        else:
            print("请选择正确的编号")

run()