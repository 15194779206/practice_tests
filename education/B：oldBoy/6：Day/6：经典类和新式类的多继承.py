
#经典类
class People:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
        self.friends=[]
    def eating(self):
        print("%s is eating"%self.Name)
#多继承类
class OBject(object):
    def make_friends(self,obj):  #obj相当于调用m1.Name
        #新式类方法中调用的参数为子类中调用的父类先执行，其中包括这个参数
        print("%s is make friends %s"%(self.Name,obj.Name))
        self.friends.append(obj) #把朋友添加到列表中,此处添加的是内存地址，防止实例化的做修改


class Women(People,OBject): #注意执行顺序，把有构造函数的放在前面
    #重构构造函数
    def __init__(self,name,age,bron,hua):
        super(Women,self).__init__(name,age)
        self.Bron=bron
        self.Hua=hua

    def Bron(self):
        print("%s one day is brning"%self.Name)

class Man(People,OBject):
    def chou(self):
        pass

p1=People("lili",22)

w1=Women("zhangnan",26,1991,"BB妆")
w1.eating()

m1=Man("liuyang",25)
w1.make_friends(m1)
print(w1.friends)  #结果：[<__main__.Man object at 0x0000000002616668>]
print(w1.friends[0].Name)  #结果 liuyang