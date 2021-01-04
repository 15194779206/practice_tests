'''
1:写一个生成器函数 my_integer(n)生成1到n的整数：
2:写入一个生成器函数,myodd(start,stop)
  用于生成start 开始到 stop结束(不包含stop)的所有奇数
'''
def my_integer(n):
    i=1
    while i<n:
        yield i
        i+=1
for x in my_integer(5):
    print(x,end=' ')

def myodd(start,stop):
    start = 1
    while start < stop:
        if start %2==1:
            yield start
        start += 1

L=[x for x in myodd(1,10)]
print(L)