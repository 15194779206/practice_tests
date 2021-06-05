def fun01(a,b,c):
    print(a,b,c)

#1位置参数
fun01(1,2,3)

#2序列参数
list_num = [1, 2, 3]
fun01(*list_num)

#3关键字传参
fun01(a=1,b=2,c=3)

#4字典关键字传参
d={"b":2,"c":3,"a":1}
fun01(**d)


#5默认参数（缺省参数）
def fun02(b, a=5, c=7): #位置参数要在关键字参数前面
    print(b, a, c)

fun02(2)
fun02(*[8,9])
fun02(**{"b":8})


def fun02(day=0,hour=0,min=0):
    days =day*24*60*60
    hours = hour*60*60
    mins =min*60
    return days+hours+mins


all =fun02(min=2)
print(all)


def fun03(*args,a,b):
    print(a)
    print(b)

fun03(a=1,b=2)

#星号元祖形参
def fun04(*args):
    print(args)

fun04(1,2,3,4,5,6)  #( 1, 2, 3, 4, 5, 6)

#双星号字典形参
def fun05(**kwargs):
    print(kwargs)

fun05(a=1,b=2) #{'a': 1, 'b': 2}
fun05(**{"a":1,"b":2}) #{'a': 1, 'b': 2}


def fun06(*args,**kwargs):
    print(args)  #(1, 2, 3)
    print(kwargs) #{'a': 1, 'b': 2}


fun06(1,2,3,a=1,b=2)


def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun07(1,2,3,4,5,c=4,d=5)



def myfun(a,*args,k): #*后面的形参使用关键字传参
    print('a=',a,'k=',k)
#myfun(1,2)#错误
myfun(1,k=2) #k强制使用关键字传参
myfun(10,**{'k':20})  #字典关键字传参

print()
