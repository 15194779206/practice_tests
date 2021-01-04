def fils():
    print("测试引用")
fils()
# __all__=['fun1','name1']   #此用于只显示all列表中的模块
def fun1():
    pass
def fun2():
    pass
def fun3():
    pass
name1='aaa'
name2='bbb'

#测试隐藏属性

def _fun4():
    pass