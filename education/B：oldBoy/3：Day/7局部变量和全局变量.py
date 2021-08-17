#局部变量在函数中声明
#全局变量在函数外声明的变量，作用域为全局

name="张三"

def core(name):
    name="lisi"
    print("my name is %s"%name)

core(name)
print(name)