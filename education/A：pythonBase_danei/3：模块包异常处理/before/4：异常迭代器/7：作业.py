'''
练习：
  1.一个球从100米高度落下，每次落地后反弹高度为原高度的一半，在落下
    1）写程序算出皮球从第十次落地后反弹的高度是多少？
    2）球共经过多少米路径
 2.打印九九乘法表
    1*1=1
    1*2=2 2*2=4
    1*3=3 2*3=6 3*3=9
 3.分解质因数
    输入一个正整数，分解质因数：
       输入：90 则打印： 90=2*3*3*5
    质因数是指最小能被原数整除的素数（不包含1）
'''

print("第一题")
def gaodu(n):
    for x in range(0,10):
        n=n/2
    print('第十次的高度是：',n)

def sums(n):
    num=0
    for x in range(0, 10):
        num += n
        n=n/2
        num += n
    print('高度总和是：',num)
n=float(input("输入高度："))
gaodu(n)
sums(n)

print("第二题")
def table_cale():
   for x in range(1,10):
       for z in range(1,x+1):
           print('%s*%s=%s'%(z,x,z*x),end=' ')
       print( )  #在第二层循环结束加空格
table_cale()


print("第三题")
def zhishu(num):
    L=[]
    for x in range(0,num+1):
        if x %2==1:
            L.append(x)
            if x *2==num:
                print(x)
    print(L)
num=int(input("请输入正整数："))
zhishu(num)