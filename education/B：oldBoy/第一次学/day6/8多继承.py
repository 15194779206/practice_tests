class School(object):
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def La(self,mm):
        print("%s mm huoqu %s"%(self.Name,mm.Name))

class Teacher(School):
    def Runing(self,ammout):
        print("one %s two %s"%(self.Name,ammout))
t1=Teacher("alex",11) #实例化
t1.Runing("say")  #调用方法将方法中的参数加入

s1=School("dada",00)
s1.La(t1)    #两个类之间产生关联