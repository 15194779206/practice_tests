#此文件讲解random模块
import random

r=random.random()
print('随机生成0-1的数：',r)
a=random.uniform(5,10)
print('指定范围内的随机数',a)
b=random.choice([1,2,6,0,8])
print('列表内随机数抽取',b)

'''
1：假设可以作为密码的字符有：
 A-Z  a-z  0-9   
 写一个程序，随机生成六位密码  
'''

def shuju(n):
    str1 = ''
    for i in range(n):  # 生成四位
        y = random.randrange(0, 6)
        if i == y:
            step = chr(random.randint(65, 90))  # 将获取的随机数转化为A-Z
        else:
            step = random.randint(0, 9)  # 生成整数随机值
        str1 += str(step)
    print("获取的验证码：", str1)

shuju(6)




