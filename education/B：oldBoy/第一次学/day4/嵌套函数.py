def foo():
    print("in the foo")
    def con(): #函数即变量，此处定义为局部变量
        print("in the con")
    con()

foo()  #打印结果in the foo   in the con