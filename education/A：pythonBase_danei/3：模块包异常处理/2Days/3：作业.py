#创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力),创建技能列表
class Skill:
    def __init__(self,id,skillname,cooltime,atk,expend):
        self.id = id
        self.skillname = skillname
        self.cooltime = cooltime
        self.atk = atk
        self.expend = expend
    def __iter__(self):
        print("%s %s %s %s %s"%(self.id, self.skillname, self.cooltime, self.atk, self.expend))

skills = [
    Skill(101, "降龙十八掌", 10, 100, 30),
    Skill(202, "凌波微步", 0, 1, 30),
    Skill(1, "一指弹", 10, 100, 0),
]

#定义函数：查找编号为101的技能对象
def selectId():
    for item in skills:
        if item.id ==101:
            yield item
for item in selectId():
    print(item.id,item.skillname,item.cooltime,item.atk,item.expend)


#定义函数：查找冷却时间为0的所有技能对象
def cooltime():
    for item in skills:
        if item.cooltime ==0:
            yield item

for item in cooltime():
    item.__iter__()

#定义函数：查找攻击力大于5的所有技能对象
def selectatk():
    for item in skills:
        if item.atk >5:
            yield item
for item in selectatk():
    item.__iter__()
#定义函数：查找攻击力大于10，并且不需要消耗法力的所有技能

def selectexpend():
    for item in skills:
        if item.atk >10 and item.expend ==0:
            yield item
for item in selectexpend():
    item.__iter__()

#使用生成器表达式练习，攻击力大于10 的对象
print("*"*40)
items = (item for item in skills if item.atk>10)
for item in items:
    print(item.skillname)