'''
1.编写函数myfac(x)计算x的阶乘 ！
   5！=5*4*3*2*1
  print(myfac(5)) #120

2.写程序算出1-20的阶乘的和
 1！+2！+3！+4！+。。。+20！
 思考，能否用函数式编程中的高阶函数实现？

 3、已知有列表：
 L=[[3,5,8],10,[[13,14],15],18 ]
   1)写一个函数print_list(lst)打印出列表中所有数字
   2)写一个函数sum_list(lst)返回列表中所有数字的和
   print(sum_list(L))  #86
  注：
    type(x)可以返回一个变量的类型
    如：
    type(20)  is int
    type([1,2,3]) is list
'''
print("======第一题=======")

def calc(n):
    if n==1:
        return 1
    return n*calc(n-1)
print(calc(5))   #结果120


print("======第二题=======")
def mysum(n):
    s=0
    for x in range(1,n+1):
        s+=calc(x)
    return s
print(mysum(3))


print("======第三题=======")
L=[[3,5,8],10,[[13,14],15],18 ]
def print_list(lst):
    for x in lst:
        if type(x) is list:
            print_list(x)  #递归进行循环
        elif type(x) is int:
            print(x)
print_list(L)

def sum_list(lst):
    s=0
    for x in lst:
        if type(x) is list:
            s+=sum_list(x)
        else:
            s+=x
    return s

print('列表相加的和为：',sum_list(L))















