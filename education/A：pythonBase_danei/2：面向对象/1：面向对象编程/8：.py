#只是通过两个方法，读写变量
'''
class Vec:
    def __init__(self,name=0,age=0):
        self.__name = name
        # self.__age = age
        self.set_age(age)

    # def get_age(self):
    #     return self.__age

    def set_age(self, value):
        if 20 <= value <=30:
            self.__age = value
        else:
            print("我不要")

w1=Vec("铁锤",81)
#print(w1._Vec__y)  #0访问私有变量
w1.set_age(80)
# print(w1.get_age())
print(w1.__dict__)  #{'x': 0, '_Vec__y': 0}





#定义敌人类
#使用属性封装变量
class diren:
    def __init__(self,name,atteck,speed,blood):
        self.name = name
        self.atteck = atteck
        self.__speed = speed
        self.set_blood(blood)

    def get_speed(self):
        return self.__speed
    def set_speed(self,value):
        if 0 <=value <=10:
            self.__speed = value
        else:
            print("已超出速度")

    def get_blood(self):
        return self.__blood
    def set_blood(self,value):
        if 0 <=value <=100:
            self.__blood = value
        else:
            self.__blood=50 #超出血量报错，但是会报错，给个默认值
            print("已超出血量")


di1=diren("张三", 100, 200, 300)
# di1.set_blood(300)
print(di1.get_blood())
print(di1.__dict__)


'''


#使用属性封装

class wife:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property  #拦截读取变量的操作
    def name(self):
        return self.__name

    @name.setter  #拦截写入变量的操作，可以做逻辑判断
    def name(self,value):
        if value !="张三":
            self.__name = value
        else:
            self.__name = "不是张三值"


w01 = wife("张三",25)

print(w01.age)

print(w01.__dict__)




#只读，或只写
#本质，创建property对象，name存储对象地址
#注意：创建对象时，会指定读取方法
#相当于 name = property(读取方法,None)
class D:
    def __init__(self,name):
        self.name = name
    def name(self,value):
        print("写入")
        self.__name = value

    name = property(None,name)
d =D("zhangsan")












