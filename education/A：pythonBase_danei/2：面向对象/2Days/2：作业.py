'''
1.使用面向对象思想，写出下列场景
    玩家（攻击力）攻击敌人，敌人受伤（血量）后掉血，还可能死亡（播放动画）
    敌人（攻击力）攻击玩家，玩家受伤（血量）后碎屏，还可能死亡（游戏结束）

2.完成学生管理器之-添加学生
'''
'''
class gameModel:
    def __init__(self, attack=0, blood=0, die=0):
        self.attack = attack
        self.blood = blood
        self.die = die
    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self,value):
        self.__attack = value

    @property
    def blood(self):
        return self.__blood
    @blood.setter
    def blood(self,value):
        self.__blood = value

    @property
    def die(self):
        return self.__die
    @die.setter
    def die(self,value):
        self.__die = value

class gameManagerController:
    def __init__(self):
        self.mode = gameModel()

    def game_attack(self):
        self.mode.attack +=10

    def low_blood(self):
        pass


class gameManagerViewer:
    def __display_menu(self):
        print("1）攻击敌人")
        print("2）攻击玩家")

    def __select_menu(self):
        number = input("请输入选择：")
        gamecontroller = gameManagerController()
        if number =='1':
            gamecontroller.game_attack()

        elif number =='2':
            gamecontroller.low_blood()

    def main(self):
        self.__display_menu()
        self.__select_menu()

managerViewer = gameManagerViewer()
'''

class player:
    def __init__(self,hp=0,atk=0):
        self.atk = atk
        self.hp=hp

    def attack(self,enemy):  #攻击
        print("打你")
        enemy.damage(self.atk)

    def damage(self,enemy_value): #受伤
        self.hp -=enemy_value
        print("受伤啦")
        if self.hp<=0:
            self.__die()

    def __die(self):
        print("玩家死亡")


class Enemy:
    def __init__(self,hp=0,atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self,player):
        player.damage()

    def damage(self,atk_value):
        self.hp -=atk_value
        print("受伤啦")
        if self.hp <=0:
            self.__die()

    def __die(self):
        print("敌人死亡")

p01 =player(100,50)
e01 = Enemy(100,50)
p01.attack(e01)

