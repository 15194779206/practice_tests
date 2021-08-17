'''
 语法：
             return  [ 表达式 ]
                  注：[ ] 代表其中的内容可以省略
                 作用：
              用于函数中，结束当前函数的执行，返回到调用函数的地方，同时返回一个对象的引用关系
                 说明：
            1、return 语句后跟的表达式可以省略，省略后相当于return  none
            2、如果函数内没有return语句，则函数执行完最后一条语句后返回none(
                 相当于在最后加了一条return  none  语句)
            3、函数调用能够返回一个对象的引用
'''
def  mymax(a,b):
    if a>b:
        return print(a)
    else:
        return print(b)

mymax(10,20)

#2:写一个函数input_number()
# 此函数用于读取用户输入的多个整数（用户输入负数时结束输入）
#将用户输入的数形成列表返回给调用者
def input_number():
    L=[]
    while True:
        num = int(input("输入数字："))
        if num >= 0:
            L.append(num)
        else:
            return print('L的列表为：',L,
                         '\n','最大值是：',max(L),
                         '\n','和是：',sum(L))
    else:
        print("输入不符合要求")
input_number()