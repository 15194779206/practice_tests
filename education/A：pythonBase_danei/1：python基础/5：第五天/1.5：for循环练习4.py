'''
练习：
  写一个程序，求1-100之间所有不能被5,7,11整除的数的和
'''
sum=0
for con in range(1,10):
    if con % 5 == 0 or con %7 == 0 or con %11 == 0:
        continue
    sum+=con
else:
    print(sum)

