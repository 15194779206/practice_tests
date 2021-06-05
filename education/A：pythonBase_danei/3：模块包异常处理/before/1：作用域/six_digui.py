'''
示例：
  求 100+99+98+。。。。+1的和

'''
l=sum([x for x in range(1,101)])  #第一种方法
print(l)
def mysum(x):
    if x==1:
        return 1
    return x + mysum(x-1)

print(mysum(100))