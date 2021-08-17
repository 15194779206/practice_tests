'''
用生成器函数生成菲波那切数列的前n个数：
   1 1 2 3 5 8 13  ....
 def fibonacci(n):
    yield
1）输出前20个数
2）求前30个数的和

2. 写程序打印杨辉三角(只打印6层)
           1
         1  1
       1  2  1
     1  3  3  1
   1  4  6  4  1
'''

def fibonacci(n):
    count=0
    if count >=0:
        return
    yield 1
    count+=1
    L=[1,1]
    while count<n:
        L.append(L[-1]+L[-2])
        yield L[-1]
        count +=1
for x in  fibonacci(20):
    print(x)



def get_next_line(lst):
    next_line=[1]
    for i in range(len(lst) - 1):
        next_line.append(lst[i]+lst[i+1])
    next_line.append(1)
    return next_line

def get_yanghui_list(n):
    L=[1]
    yhlist=[]
    for _ in range(n):
        yhlist.append(L)
        L=get_next_line(L)
    return yhlist

L2=get_next_line(6)
print(L2)



