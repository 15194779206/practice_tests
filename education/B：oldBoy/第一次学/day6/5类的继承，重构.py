class People:
    #构造函数函数实例化变量
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    #定义方法
    def All(self):
        print("%s is eating"%self.Name)
    #定义方法被子类重构
    def Tall(self):
        print("%s is taller"%self.Age)

class Man(People):
    def Huzi(self):
        print("all man %s has"%self.Name)

#子类重构父类方法
class Woman(People):
    #Tall为父类的方法。People为父类
    def Tall(self):
        People.Tall(self)
        print("man is older")

#子类重构父类的构造函数
class Animals(People):
    #子类重构父类的时候，要先把父类的方法拿下来
    def __init__(self,name,age,zilei):
        People.__init__(self,name,age)
        self.ZIlei=zilei
        print("zilei is %s"%self.ZIlei)

#多重继承
class Relation(object):
    def __init__(self,n1,n2):
        print("init in relation")
    def make_friends(self,obj): #w1
        print("%s is making friends with %s" % (self.name,obj.name))
        self.friends.append(obj.name)
class Duo(Relation,People):
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)

p1=People("zhangsan",22)
p1.All()
p1.Tall()
#子类的调用
m1=Man("lisi",11)
m1.All()
m1.Huzi()
m1.Tall()

#子类重构父类方法
w1=Woman("ala0",33)
w1.Tall()

#子类重构父类的构造函数
a1=Animals("anla",22,"tt")
print(a1.ZIlei)

#多重继承显示

d1=Duo("duochong",100)
