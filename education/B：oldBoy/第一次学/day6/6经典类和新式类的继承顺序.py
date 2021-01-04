#继承的策略
  #广度优先和深度优先
class A:
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    def __init__(self):
        print("C")
class D(B,C):
    pass
    # def __init__(self):
    #     print("D")


obj = D()
