'''
1.输入一个圆的半径，打印出这个圆的面积
'''
import math
#求面积
r=int(input("半径："))
s=round((math.pi*r**2),2)
print(s)

#求半径
s=float(input("输入面积："))
r=math.sqrt(s/math.pi)
print(r)