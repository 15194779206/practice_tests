#1：装饰器验证登录功能

user="alex"
passw='abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):   #此层是装饰器中添加参数，需要在嵌套一层
        def wrapper(*args, **kwargs):
            print("wrapper func args:",*args, **kwargs)
            if auth_type=="local":
                username = input("输入姓名：").strip()
                password = input("输入密码：").strip()
                if user == username and passw == password:
                    print("欢迎登录")
                    # func(*args,**kwargs)  #执行每个模块自己的功能
                    # 如果函数内部含有返回值，此处需要进行返回
                    res = func(*args, **kwargs)
                    print("----此处内容home()de return-----")
                    return res
                else:
                    exit("验证失败")
            else:
                print("in the ldap")

        return wrapper  # 返回值返回的是函数名
    return outer_wrapper

#下面的函数在模拟页面
def index():
    print("in the index")

#两个函数中，一个本地认证，一个ldap认证
#如果装饰器中含有参数，需要在嵌套一层
@auth(auth_type='local')
def home():
    print("in the home")
    return  "def return home"

@auth(auth_type='ldap')
def bbs():
    print("in the bbs")

index()
print(home())
bbs()
