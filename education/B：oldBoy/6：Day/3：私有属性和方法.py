class Role:
    def __init__(self,name,age):
        self.Name=name   #公有属性
        self.__Age=age   #是有属性


    def Pron(self):
        print("%s is too older"%self.__Age)
r1=Role("zhangsan",22)
print(r1.Name)
#print(r1.__Age)  #不可进行访问，如果需要打印，可以放在方法中进行打印输出
r1.Pron()  #此方法为了打印带有的私有属性