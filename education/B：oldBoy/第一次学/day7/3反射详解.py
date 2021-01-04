def bulk(self):
    print("%s is yelling...." %self.name)

class Att(object):
    def __init__(self,name):
        self.Name=name
    def eat(self):
        print("%s is eating..."%self.Name)
    def dele(self):
        print("此模块测试删除！")

a=Att("zhangsan")
choice=input(">>:").strip()
if hasattr(a,choice):
    getattr(a,choice)()
    # delattr(a, choice)
else:
    setattr(a,choice,bulk)
    func = getattr(a, choice)
    func(a)
