#定义一个类，把具有相同操作的放到一个类中

class Juji:
    shot="lone"   #类变量
    def __init__(self,name,fire,money=15000):
        self.Name=name  #属性，实例变量
        self.Fire=fire

    def got_shot(self):
        print("%s got shot" %self.Name)

    def Huoli(self,gun_name): #自身定义参数 gun_name
        print("%s is %s fire,game is %s" %(self.Name,self.Fire,gun_name))


r1=Juji("zhangsan",1000)
r1.got_shot()
r1.Huoli('Ak47')