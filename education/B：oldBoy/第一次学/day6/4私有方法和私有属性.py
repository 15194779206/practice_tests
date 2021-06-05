#私有方法和私有属性在变量前面加两个下划线    _ _

class People:
    def __init__(self, name, age):
        #将姓名私有化
        self.__Name=name
        self.Age=age

    def Run(self):
        #私有化的属性放在方法中可以进行使用
        print("one people run is %s"%self.__Name)
    def __Jump(self):
        print("%s is older"%self.Age)

r1=People("alex",22)
r1.Run()
r1. __Jump()  #私有化的方法不能再调用