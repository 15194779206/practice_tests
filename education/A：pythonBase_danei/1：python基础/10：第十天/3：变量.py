'''
查找规则：
  1)查找本地变量     2) 查找包裹此函数的外部嵌套函数内部的变量
  3)全局变量         4) 内置变量
'''
a=100
b=200
def fx(b,c):
    print(a,b,c)
fx(300,400)  #100 300 400

'''
1：写一个函数mysum 此函数的功能时返回：1+2+3+4.。。。+n的和
'''
L=[]
def mysum(n):
    for i in range(n+1):
        L.append(i)
    print(sum(L))
mysum(100)

'''2：写一个函数mysum2
此函数可以传入一个参数，两个参数和三个参数：
1）当传入一个参数时，这个参数代表终止数
2）当传入两个参数时，第一个参数代表起始值，得个参数代表终止值
3）当传入三个参数时，代表步长
此函数的功能时返回从开始到终止值的和：
'''
'''
def mysum2(*args):
    s = 0
    if len(args)==1:
        for i in range(args[0]):
            s += i
        print(s)
    elif len(args)==2:
        for i in range(args[0],args[1]):
            s += i
        print(s)
    elif len(args)==3:
        for i in range(args[0],args[1],args[2]):
            s += i
        print(s)
'''
def mysum2(*args):
    s = 0
    if len(args)==1:
        x=range(args[0])
    elif len(args)==2:
        x=range(args[0],args[1])
    elif len(args)==3:
        x=range(args[0],args[1],args[2])
    for i in x:
        s += i
    print(s)
#方法2
def  my(*args):
    print(sum(range(*args)))

mysum2(11)
mysum2(1,10)
mysum2(1,10,2)







