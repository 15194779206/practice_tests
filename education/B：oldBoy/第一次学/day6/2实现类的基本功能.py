class Role(object):
    #用于存放参数
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name11 = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("%s:ah...,I got shot..."%self.role)

    def buy_gun(self):
        print("just bought %s"%self.name11)

#实例化（初始化一个类，造了一个对象），生成一个角色
r1 = Role('Alex', 'police', 'AK47')
r1.got_shot()
r1.buy_gun()