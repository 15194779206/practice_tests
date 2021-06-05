import time

# 装饰器
name='alex'
age='123'
def time(func):
    def conn(*args,**kwargs):
        # 放入参数组，是为了防止被装饰的函数含有参数，所以此处添加
        username=input("username:").strip()
        userpass=input("password:").strip()
        if username==name and userpass ==age:
            print("success")
        else:
            print("password or username is wrong")
    return conn
#设计一个页面为一个函数
@time
def index():
    print("I am a index")

index()