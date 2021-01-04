"""
实现装饰器的知识储备：
1：函数即变量
2：装饰器
3：嵌套函数
"""
#匿名函数，匿名函数的意思就是函数没有名字，
calc=lambda x:x*3
print(calc(3))   #结果9

#高阶函数，把函数名当做变量进行传递
def bar():
    print("in the bar")
def test1(func):
    print(func)  #in the bar
    func()    #<function foo at 0x000000000250DC80>内存地址

test1(bar)



def foo():
    pass
print(foo)   #<function foo at 0x00000000021ADB70>获取的是内存地址
#foo()在内存地址上进行调用操作