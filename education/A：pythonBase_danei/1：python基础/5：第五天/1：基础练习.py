num01=0xa  #16进制
print(num01)

a=100
b=120
c=a
del a,b
print(c)

a=100
b=120
c=a
del a,b
print(c)

s1="10"
s2=10
print(type(s1))  #<class 'str'>
print(type(s2))  #<class 'int'>
#复数
s3=1j
print(type(s3))  #<class 'complex'>

#input输出的结果是str类型
# s6 = input("age:")
# print(type(s6)) #<class 'str'>
'''
name = input("name:")
age = int(input("age:"))
sex = input("sex:")
score = float(input("score:"))
print("name:"+name, "age:"+str(age), "sex:"+sex, "score:"+str(score))
'''
'''
price = int(input("price:"))
count = int(input("count:"))
money = int(input("money:"))
only_money = money-price*count
print(only_money)
'''
height = int(input("height:"))
jin = height//16
liang = height%16
print(str(jin)+"斤"+str(liang)+"两")