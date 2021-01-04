'''
内置函数：map   filter  sorted
'''

#生成一个可迭代对象，要求此可迭代对象可以生成1-9自然数的平方
print("=========map函数===========")
def power2(x):
    return x**2
for x in map(power2,range(1,10)):
    print(x,end=' ')  #1 4 9 16 25 36 49 64 81
print(sum(map(power2,range(1,10))))  #求和285

#map()函数练习
#1：求1**2 +2**2+3**2+4**2......9*2的和
print(sum(map(pow,range(1,10),[2,2,2,2,2,2,2,2,2,2])))#285
#2：求 1**3+2**3+....9**3的和
print(sum(map(pow,range(1,10),[3,3,3,3,3,3,3,3,3,3]))) #2025
#3：求 1**9 +2**8+3**7......9**1的和
print(sum(map(pow,range(1,10),range(9,0,-1))))#11377

print("==========filter讲解===========")
#生成10以内所有偶数的列表，用filter实现
def isde(x):
    return x%2==0
for x in filter(isde,range(10)):
    print(x,end=' ')


print("==========sorted讲解===========")
L=[1,-2,3,-4,5]
L2=sorted(L,key=abs)
print(L2)  #[1, -2, 3, -4, 5]v

names=['Tom','Jerry','Spike','Tyke']
L=sorted(names,key=len)
print(L)





