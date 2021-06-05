#raise 需要结合 try-except使用
def make_except(n):
    print("begin...")
    if n<0:
        raise ValueError("输入的值%s小于约定值"%n)
    print('end')

value=int(input("输入数值："))
try:
    make_except(value)
except ValueError as e:
    print("错误类型:",e)
