'''
try:
    可能触发的异常语句
except 错误类型1[as 变量1]:
    异常处理语句1
except 错误类型x[as 变量x]:
    异常处理语句x
else:
    未发生异常的语句
finally:
    最终语句
'''
def div_apple(n):
    print("%d个苹果你想要分给几个人？"%n)
    s=input("请输入人数：")
    cnt=int(s)
    result=n/cnt
    print("每个人分了",result)

try:
    div_apple(10)
except ValueError as err:
    print("异常错误")
    print("错误值：",err)
except ZeroDivisionError:
    print("发生零输入值的错误")
else:
    print("没有发生错误执行语句")
finally:
    print("finally语句")


print("程序退出")