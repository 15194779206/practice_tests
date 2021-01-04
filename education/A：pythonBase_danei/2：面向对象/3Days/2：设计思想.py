'''
手雷爆炸，可能伤害敌人，玩家；还有可能伤害未知事物（鸭子，树，房子）
要求：如果增加了新的事物，手雷代码不变
'''
'''

class Grenade:
    # 手雷
    def __init__(self,atk):
        self.atk = atk

    def explode(self,*args):
        for item in args:
            if not isinstance(item,Damageable):
                print("类型不兼容")
                return
            item.damage(self.atk)

class Damageable:
    # 可以受伤
    def __init__(self,hp):
        self.hp =hp

    def damage(self,value):
        self.hp -=value

class Player(Damageable):
    def damage(self,value=0):
        super().damage(value)
        print("碎屏")

class Enemy(Damageable):
    def damage(self,value):
        super().damage(value)
        print("播放动画")

g01 =Grenade(10)
p02 =Player(100)
e03 = Enemy(50)
g01.explode(p02,e03)
'''
# raise.NotImplementedError


class Grenade:  #手雷
    def __init__(self,value):
        self.value = value

    def grenade(self,*args):
        for item in args:
            item.injured(self.value)


class Injured: #父类受伤
    def __init__(self,hp):
        self.hp = hp

    def injured(self,value):
        self.hp -= value
        # 约束子类，必须有父类的方法
        # raise NotImplementedError


class Damage(Injured): #子类敌人受伤
    def injured(self, value):
        # self.hp -= value
        super().injured(value)  #调用父类的方法，进行减血
        print("敌人受伤,剩余血量",self.hp)

class Player(Injured): #子类玩家受伤
    def injured(self, value):
        # self.hp -= value
        super().injured(value)  # 调用父类的方法，进行减血
        print("玩家受伤,剩余血量",self.hp)

in01=Injured(100)  #受伤
p01 =Player(100)
d01 =Damage(200)
Gr01 =Grenade(20)  #手雷
Gr01.grenade(p01,d01)  #玩家受伤,剩余血量 80   敌人受伤,剩余血量 180





