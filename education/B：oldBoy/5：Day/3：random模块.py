import random

#1：生成0-1之间的随机浮点数
x=random.random()
print("随机浮点数：",x)
#2:指定范围内的随机浮点数
y=random.uniform(0,9)
print("指定范围内随机浮点数：",y)
#3:指定范围内的整数
z=random.randint(0,100)
print("指定范围内随机整数：",z)
#4:指定范围内，按指定基数递增的集合中，获取一个随机数
y=random.randrange(0,4)
print("获取随机数randrange：",y)
#5:从序列中获取一个随机元素
a=random.choice('abcf')
print("获取指定范围内随机元素：",a)


#小测试，随机生成验证码测试
str1=''
for i in range(4):  #生成四位
    y=random.randrange(0,4)
    if i == y:
        step = chr(random.randint(65, 90))  # 将获取的随机数转化为A-Z
    else:
        step = random.randint(0, 4)  # 生成整数随机值
    str1 += str(step)
print("获取的验证码：", str1)
