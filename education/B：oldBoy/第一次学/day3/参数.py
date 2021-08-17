
# 形参和 实参一一对应
def test(x,y):
    print(x)
    print(y)
test(1,2)

# 如果不一一对应，直接赋值
test(y=3,x=5)

# 实参对应和直接赋值混用
# test(x=2,3)  #报错，关键参数不能写在位置参数前面
test(6,y=7)  #test(位置参数，关键参数)

# 默认参数的用途
def conn(x,y=1):
    print(x)
    print(y)

conn(2,2)


# 实参不固定
# 所以用*args表示参数组接收，返回元组
def  Content(x,*args):
    print(x,args)
Content(1,2,3,4,5,5)          #输出内容为1 (2, 3, 4, 5, 5)

def  Tent(**kwargs):
    print(kwargs)

Tent(name="alex",age=21)     #返回内容 {'name': 'alex', 'age': 21}
#也可以这样写
Tent(**{'name':'alex','age':12})


# 接收字典存在默认参数
# def Conte(age=18,name,**kwargs):   位置参数在关键字之前
def Conte(name,age=18,**kwargs):
    print(name,age,kwargs)
#    输出值的两种写法
Conte("alex",**{'lala':"zhangsa",'fan':"12"})
Conte("alex",lala="zhangsa",fan="12")

# 两种参数组混用
def hunhe(*args,**kwargs):
    print(args)
    print(kwargs)
hunhe(1,2,3,zhang='1',nale="lala")