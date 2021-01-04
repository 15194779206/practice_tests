def myield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成4")
    yield 4
    print("生成器函数调用结束")

gun=myield()
it=iter(gun)
print(next(it))