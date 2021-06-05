gen=(x**2 for x in range(0,5))
it=iter(gen)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration as err:
    print("执行到最后一条啦,此处不写异常会报错")