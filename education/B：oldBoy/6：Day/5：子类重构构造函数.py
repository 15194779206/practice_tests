#经典类
class People:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def eating(self):
        print("%s is eating"%self.Name)

class Man(People):
    #重构构造函数
    def __init__(self,name,age,bron,hua):
        super(Man,self).__init__(name,age)
        self.Bron=bron
        self.Hua=hua

    def Bron(self):
        print("%s one day is brning"%self.Name)

p1=People("lili",22)

m1=Man("zhangnan",26,1991,"BB妆")
m1.eating()
