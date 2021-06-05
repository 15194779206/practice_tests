'''
1:定义父类：武器，
    数据：攻击力
    行为：购买（所有子类都一样），攻击（不知道怎么攻击）
  定义子类：枪
    数据：射速
    行为：攻击
  定义子类：手雷
    数据：爆炸范围
    行为：攻击
创建相应对象，调用相应方法
'''

#打击敌人
class Fight_enemy:
    def __init__(self, hps, enemy_dis):
        self.hps = hps
        self.enemy_dis = enemy_dis

    def distance_en(self,weapons):
        weapons.attacks(self.enemy_dis,self.hps)

#武器
class Weapons:
    def __init__(self,attack):
        self.attack = attack

    def buying(self):
        raise  NotImplementedError()

    def attack(self,*args):
        raise NotImplementedError()

#手枪
class Guns(Weapons):
    def __init__(self, speed, attack):
        super().__init__(attack)
        self.speed = speed

    def attacks(self,value_dis,hp): #与敌人之间的距离
        if value_dis > self.speed:
            print("敌人距离太远")
            return
        elif value_dis <=self.speed:
            print("敌人被射击")
            hp -=self.attack
            if hp <=0:
                print("敌人死亡")


#手雷
class Grenades(Weapons):
    def __init__(self,distance,attack):
        super().__init__(attack)
        self.distance = distance


    def attack(self,value_dis,hp):
        pass

en01 = Fight_enemy(100, 30)
gun01 = Guns(10, 10)
en01.distance_en(gun01)




















