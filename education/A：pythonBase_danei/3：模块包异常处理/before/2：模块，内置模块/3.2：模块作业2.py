'''
1：请编写函数fun其功能时计算并输出下列多项式的和
Sn = 1/1! +1/2! +... 1/n!

2：请编写函数fun , 他的功能时计算下列多数项的和并返回：
s=1+x+x**2/2！ +x**3/3!+  x**n/n!
'''

import math

def fun(n):
    sum = 0
    for x in range(n+1):
        sum+=1/math.factorial(x)
    print(sum)
fun(20)

#方法2
def fun(n):
    s=sum(map(lambda x:1/math.factorial(x),range(n)))
    print(s)
fun(20)
