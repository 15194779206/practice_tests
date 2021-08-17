def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 函数变成生成器，只需要将print(b)改为yield
        # print(b)
        yield b
        # a, b = b, a + b
        # 此处相当于
        t=[b,a+b]
        a=t[0]
        b=t[1]
        n = n + 1
    return 'done'
data=fib(10)
print(data)
print(data.__next__())
print(data.__next__())
#函数生成式
reg=(i*2 for i in range(10))
print("--------")
for n in reg:
    print(n)