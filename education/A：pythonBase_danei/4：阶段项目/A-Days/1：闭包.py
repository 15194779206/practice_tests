def fun01():
    a=11
    def fun02():
        print("变量",a)
        print("fun02的值")
    return fun02
re = fun01()
re()