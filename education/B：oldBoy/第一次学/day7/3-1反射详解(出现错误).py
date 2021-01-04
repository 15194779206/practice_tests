__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):
    func=getattr(d,choice)
    func("goushi")
    # delattr(d,choice)  #删除完会报错
else:
    setattr(d,choice,bulk) #d.talk = bulk
    func = getattr(d, choice)
    func(d)

