#本示例示意实例的定义方式和调用方法
class Dog:
    def __init__(self,food,hour):
        self.Food=food
        self.Hour=hour
    def eat(self):
        print("小狗吃了",self.Food)
    def sleep(self):
        print('小狗睡了',self.Hour,'小时')

dog1=Dog('骨头',1)
dog1.eat()
dog1.sleep()