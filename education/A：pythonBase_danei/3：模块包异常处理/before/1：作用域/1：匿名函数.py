'''
①作用：
   创建一个匿名函数对象
   同def类似，但不提供函数名
②语法：
   lambda[形参1，形参2，。。。] :表达式
'''
'''
1:写一个lambda表达式，判断这个数的2次方+1
能否被5整除，如果能整除返回True，否则返回false
'''
fx=lambda n:(n**2+1)%5==0
print(fx(1))

'''
2:写一个lambda表达式，求两个变量的最大值：
mymax=lambda....
print(mymax(55,63))
'''
mymax =lambda x,y:x if x>y else y
print(mymax(55,63))












