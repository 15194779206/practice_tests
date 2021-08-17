class People:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def sleep(self):
        print("%s is sleeping"%self.Name)
    def run(self):
        print("%s is running"%self.Name)

class Women(People):
    def zhuang(self):
        print("%s is huazhuang"%self.Name)
    def sleep(self):
        People.sleep(self)  #先执行父类的方法
        print("子类重构父类，此处不进行覆盖，父类和子类都运行") #在执行子类添加的方法

#子类的继承
w1 =Women("zhangsan",22)
w1.sleep()
w1.zhuang()