'''
 [  表达式   for  变量  in   可迭代对象 ]或
[  表达式   for  变量  in   可迭代对象   if  真值表达式]
'''
#1：用列表推导式生成1-100内奇数的列表
#判断奇数 %2=1是奇数   %2=0是偶数
L=[x for x in range(10) if x%2==1]
print(L)

'''
练习：
   输入一个数值作为开始的数，用begin开始
   在输入一个结束的整数用end绑定
    将开始至结束的数中，平方加1能被5 整除的数放入列表中
    例如：
     请输入开始数：1
     请输入结束数：20
'''
begin=int(input("请输入开始数："))
end =int(input("请输入结束数："))
L=[x for x  in range(begin , end) if ((x**2+1)%5==0)]
print(L)






