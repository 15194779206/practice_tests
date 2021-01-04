'''
张三教李四学习python
李四教张三玩游戏
张三工作转了8000元
李四工作赚了3000元


class Person:
    def __init__(self,name):
        self.name = name
        self.age = 10
        self.__skills = []  #写成私有变量，只读操作
        self.total_money = 0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def skill(self):
        return self.__skills[:]#返回新的可变对象地址
        # return self.__skills返回可变对象地址，意味着类外仍然可以操作

    def teach(self,person_other,str_skill):
        person_other.skills.append(str_skill)
        print(self.name,"教了",person_other.name,str_skill)

    def money(self,money):
        self.total_money +=money
        print("%s赚了%s元"%(self.name,money))

zs = Person("张三")
ls = Person("李四")
zs.teach(ls,"python")
ls.teach(zs,"游戏")
zs.money(1000)
'''

'''
创建技能类(技能名称，冷却时间，持续时间，攻击距离。。。)
要求：使用属性分装变量
创建技能列表（技能对象的列表）
--查找名称是“降龙十八掌”的技能对象
--查找名称是持续时间大于10秒的所有技能对象
--查找攻击距离最远的技能对象
--按照持续时间，对列表升序排列
'''
class SkillData:
    def __init__(self, name, cd, time, atk_distance):
        self.name = name
        self.cd = cd
        self.time = time
        self.atk_distance = atk_distance
        # self.skill_list = []
    def print_self(self):
        print(self.name,self.cd,self.time,self.atk_distance)

    # def skill(self):
    #     self.skill_list.append(self.name)
    #     self.skill_list.append(self.cd)
    #     self.skill_list.append(self.time)
    #     self.skill_list.append(self.atk_distance)
    #     print(self.skill_list)

skill_list=[
    SkillData("降龙十八掌", 10, 20, 100),
    SkillData("凌波微步", 5, 5, 20),
    SkillData("六脉神剑", 15, 10, 50),
    SkillData("易容术", 3, 15, 10)
]
# --查找名称是“降龙十八掌”的技能对象
for item in skill_list:
    if item.name == "降龙十八掌":
        item.print_self()
# --查找名称是持续时间大于10秒的所有技能对象
list =[]
for item in skill_list:
    if item.time >10:
        list.append(item)
for result in list:
    result.print_self()
# --查找攻击距离最远的技能对象
print("="*20)
dis = skill_list[0]
for i in range(1, len(skill_list)):
    if skill_list[i].atk_distance > dis.atk_distance:
        dis = skill_list[i]
dis.print_self()

# --按照持续时间，对列表升序排列
print("*"*20)
for i in range(len(skill_list)-1):
    for y in range(i+1, len(skill_list)):
        if skill_list[i].cd > skill_list[y].cd:
            skill_list[i],skill_list[y] = skill_list[y],skill_list[i]

for item in skill_list:
    item.print_self()




#创建技能类(技能名称，冷却时间，持续时间，攻击距离。。。)
# 要求：使用属性分装变量
# 创建技能列表（技能对象的列表）
# --查找名称是“降龙十八掌”的技能对象
# --查找名称是持续时间大于10秒的所有技能对象
# --查找攻击距离最远的技能对象
# --按照持续时间，对列表升序排列