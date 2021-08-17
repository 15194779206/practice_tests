def  get_age():
    a=input("请输入年龄：") #输入140
    a=int(a)
    assert a<140,"年龄不可能大于140"  #报错，出现AssertionError: 年龄不可能大于140
    assert a>=0,"年龄不可能出现负数"
    return a
try:
    age=get_age()
    print("您的年龄是：", age)
except AssertionError as err:
    print("输入类型错误",err)


