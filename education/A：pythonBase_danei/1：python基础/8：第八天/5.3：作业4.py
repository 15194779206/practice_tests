'''
任意输入一个数n代表三角形的高度，打印的三角形如下
输入：4
   打印如下
   1
  121
 12321
1234321
'''

num=int(input("请输入数的高度："))
for i in range(0,num):
    s=''
    for x in range(1,num+1):
        s+=str(x)
        end = ' ' * (num - i - 1)
        start = s*(2*i+1)
        print(end+start)


