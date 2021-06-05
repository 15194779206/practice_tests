'''
1：
 写一个函数 mysum , 此函数带有两个参数 x,y
  此函数功能是打印出两个参数 x,y的和，即  x+y
2：
  写一个函数print_even，传入一个数参n 代表终止整数（不包含n）
  打印：
      2 4 6 。。。n  之间所有偶数
'''
'''
def mysum(x,y):
    print(x+y)
while True:
    num1 = int(input("请输入:"))
    num2 = int(input("请输入:"))
    mysum(num1, num2)
    if num1==-1:
        break
'''
def print_even(n):
    for i in range(n):
        if i % 2 == 0:
            print(i,end=' ')

num3 = int(input("请输入:"))
print_even(num3)