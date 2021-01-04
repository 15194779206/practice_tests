'''
练习：
1:isinstance(对象，类)
2：issubclass(类，类)
'''


class  pet:
    def __init__(self,name):
        self.name =name
    def eat(self,pie):
        print("%d碗"%pie)

class Dog(pet):
    def __init__(self,name,score):
        super().__init__(name)  #调用父类的属性
        self.score = score

    def work(self):
        super().eat(3)  #调用父类的方法
        print("%s 工作"%(self.name))
class Cat(pet):
    pass

d01 =Dog("zhangsan",90)
p01 =pet("guaiguai")
c01 = Cat("lisi")
print(isinstance(d01,pet),isinstance(d01,Dog),isinstance(d01,Cat))  #True True False
print(issubclass(Dog,pet),issubclass(Dog,(pet,Cat)),issubclass(Dog,Cat)) #True True False