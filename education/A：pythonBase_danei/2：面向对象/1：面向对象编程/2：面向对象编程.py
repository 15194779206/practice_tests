'''
构造函数
'''
class Dog:
    pass
dog1=Dog()
print(id(dog1))
dog2=Dog()
print(id(dog2))
print(dog1 is dog2)
#实例有自己的作用域或名字控件，可以为该实例添加实例变量（也叫属性）
#实例可以调用类的方法
#实例可以访问类中的类变量