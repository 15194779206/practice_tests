"""
用的地方比较少：
   生成器只有在调用时才会生成相应的数据，这样不会耗费内存空间
   只记录当前位置，取到下一个数据，前一个数据不可取
   只有一个方法  _ _next_ _()
"""
#斐波那契数列
def lib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return '----done-----'
g=lib(6)
for i in g:
    print(i)