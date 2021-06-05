'''
1:写一个函数，mysum ,可以传入任意个实参的数字，返回所有实参的和
2：已知内建函数max的版主文档为：max（。。。）
    max(iterable) ->value
    max(arg1,arg2,*args) ->value
造访max,写一个mymax函数，实现功能与max完全相同
    测试用例：
       print(mymax([6,8,3.5]))  #8
       print(mymax(100,200))    #200
       print(mymax(1,3,9,7,5))  #9
3:
  写一个函数minmax
     可以给出任意个数字实参，返回这些实参的最小数和最大数，
     要求两个数字形成元组后返回，（最小数在前，最大数在后）
   调用此函数，能得到实参的最小值和最大值

'''
print("==========第一题=========")
def mysum(*args):
    return args

L=mysum(1,2,3)
print(sum(L))

print("==========第二题=========")
def mymax(*args):
    if len(args)==1:
        L = list(*args)  #存放在列表中
        L.sort()
        print('最大值是：', L[-1])
    elif len(args)>=2:
        L = list(args)
        L.sort()
        print('最大值是：', L[-1])

mymax(1,2,3,4,5)
mymax([6,8,3.5])



print("==========第三题=========")
def mymin(*args):
    L=list(args)
    L.sort()
    print('最小值和最大值是：',L[0],',',L[-1])

mymin(1,2,3,4,5)
