'''
  1.创建一个列表L=[]，写一个函数input_number读取数据放入列表L中
  2.写一个函数 isprime(x)
     判断x是否为素数，如果为素数返回True，否则返回false
    if isprime(5)
      print("5是素数")
  3.写一个函数prime_m2n(m,n)
    返回从m开始，到n结束范围内素数的列表，并打印
    L=prime_m2n(10,20)
    print(L)  #(11,13,17,19)
  4.写一个函数primes(n),返回小于n的所有的素数的列表
    L=primes(10)
    print(L)#(2,3,5,7)

'''
import sys
'''
L=[]
def  input_number():
    while True:
        i=int(input("请输入数字："))
        if i == -1 :
            break
        L.append(i)
input_number()
print(L)
'''
print("========第二题=========")
"""
x=int(input("请输入数字："))
def isprime(x):
    if x % 2 == 1:
        print("%s 是 素数" % x)
    else:
        print("%s 不是素数" % x)
isprime(x)
"""
print("==========第三题============")
"""
m=int(input("请输入起始值："))
n=int(input("请输入结束值："))
def prime_m2n(m,n):
    list = []
    for i in range(m,n):
        if i%2 ==1:
            print(i,end=' ')
prime_m2n(m,n)

"""
print("==========第四题============")

def primes(n):
    for x in range(n):
        if x % 2 == 1:
            print(x,end=' ')
primes(20)
