'''
需求：小明在招商银行取钱
分而治之--分解
变化点

1:取钱逻辑，应该有银行决定，所以取钱方法，定义在了银行
'''

class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.money =money

    # def money_les(self,bank_na):
    #     #对象b1放在p1里面，相当于b1 = bank_na,引用的是b1.bank_name
    #     print("%s 去%s取钱"%(self.name,bank_na.bank_name）)

class Bank:
    def __init__(self,bank_name,Total_money):
        self.bank_name = bank_name
        self.Total_money = Total_money


    def draw_money(self,person,value):
        if self.Total_money >person.money:
            self.Total_money -= value
            person.money += value
            print("取钱成功",self.Total_money)
        else:
            print("取钱失败")


p1 = Person("张三",100)
b1 = Bank("招商银行",10000)

b1.draw_money(p1,100)