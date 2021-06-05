'''
#1：消化2048核心算法
#2：面向对象思想，对象与对象数据不同，类与类行为不同
    张三 教 李四 学习python
    李四 教 张三 玩游戏
    张三 工作 赚了 8000元
    李四 工作 赚了 3000元

#3：创建技能类（技能名称，冷却时间，持续时间，攻击距离....）
    :要求：使用属性封装变量
    创建技能列表（技能对象的列表）
    --查找名称是"降龙十八掌"的技能对象
    --查找名称是持续时间大于10秒的所有技能对象
    --查找攻击距离最远的技能对象
    --按照持续时间，对列表升序排序
'''

'''
class Doing:
    def __init__(self, name):
        self.name = name
        self.__skills = []
        self.total_money = 0

    @property  #只读属性
    def skills(self):
        # return self.__skills[]  #返回可变对象地址，意味着类仍然可以操作
        return self.__skills[:] #返回新的可变对象地址，意味着类外仍然操作
    def teach(self, person, skill):
        person.skills.append(skill)
        print(self.name, "教", person.name, skill)

    def work(self, money):
        self.total_money +=money
        print(self.name, "工作赚了", money, '元')

zs =Doing("张三")
ls =Doing("李四")
zs.teach(ls,'python')
zs.teach(ls,'java')
zs.work(800)

'''


class  skill:
    def __init__(self,skill_name, cool_time, duration_time, distance):
        self.skill_name = skill_name
        self.cool_time = cool_time
        self.duration = duration_time
        self.distance = distance

    @property
    def skill_name(self):
        return self.__skill_name

    @skill_name.setter
    def skill_name(self,value):
        self.__skill_name = value



    def print_self(self):
        print(self.skill_name,self.cool_time,self.duration,self.distance)


skill_list=[
    skill("降龙十八掌",200,20,10),
    skill("凌波微步",100,40,20),
    skill("羞羞铁拳",100,30,30)
]

# --查找名称是"降龙十八掌"的技能对象

'''
#     --按照持续时间，对列表圣墟排序
for i in skill_list:
    if i.skill_name =="降龙十八掌":
        i.print_self()

#     --查找名称是持续时间大于10秒的所有技能对象
dur_list = []
for dur_time in skill_list:
    if dur_time.duration >10:
        dur_list.append(dur_time)

for y in dur_list:
    y.print_self()


# 查找攻击距离最远的技能对象
result = skill_list[0]
for i in range(1, len(skill_list)):
    if result.distance < skill_list[i].distance:
        result = skill_list[i]


result.print_self()

'''

#按照持续时间，对列表升序排序
