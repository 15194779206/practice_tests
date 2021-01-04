#练习


class SkillData:
    def __init__(self,id,name,cd,atk,costSP):
        self.id =id
        self.name = name
        self.atk = atk
        self.cd = cd
        self.costSP = costSP
list_skills =[
    SkillData(101,"降龙十八掌",60,10,5),
    SkillData(102,"天龙八部",50,15,0),
    SkillData(103,"如来神掌",0,20,8),
    SkillData(104,"一阳指",15,30,9),
]



#查找编号是101的技能对象
#查找名称是"降龙十八掌"的技能对象
#查找cd大于10的技能对象

#一、初始思想
for item in list_skills:
    if item.id ==102:
        print(item.id,item.name,item.cd,item.atk,item.costSP)

for item in list_skills:
    if item.name =="降龙十八掌":
        print(item.id,item.name,item.cd,item.atk,item.costSP)


#二、公共内容提取
def searchSkill(list_target,funcs):
    for item in list_target:
        if funcs(item):
            yield item

def funcs(items):
    return items.id==102
# def funcs2(items):
#     return items.name =="降龙十八掌"

for item in searchSkill(list_skills,funcs):
    print(item.id,item.name,item.cd,item.atk,item.costSP)


#三、使用lambda提取
for item in searchSkill(list_skills,lambda items:items.id ==102):
    print(item.id,item.name,item.cd,item.atk,item.costSP)








#问题2：获取所有的技能名称
list_it = []
def lists(lists,funs):
    for item in lists:
        funs(item)
    yield list_it

# def func(item):
#     list_it.append(item.id)
# for item in lists(list_skills,func):
#     print(item)

#和上面写法一致
for item in lists(list_skills,lambda item:list_it.append(item.name)):
    print(item)

#或是可以写
def lists(lists,funs):
    for item in lists:
        yield funs(item)


for item in lists(list_skills,lambda item:item.id):
    print(item)


#问题3：求冷却时间的和
summs =[]
def summ(lists,funs):
    for item in lists:
        summs.append(funs(item))
    yield sum(summs)

for item in summ(list_skills,lambda item:item.atk):
    print(item)