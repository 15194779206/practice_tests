#定义：在函数体内，用def的形式定义一个函数
def foo():
    print("in the foo")
    def bar():
        print("in thr bar")
    bar()
foo()