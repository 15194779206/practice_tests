from Acommon.dict_ListHelper import *
class SkillData:
    def __init__(self,id,name,atk,cd,costSP):  #编号，姓名，攻击力，血量，攻击速度
        self.id =id
        self.name = name
        self.atk = atk
        self.cd = cd
        self.costSP = costSP
list_skills =[
    SkillData(101,"降龙十八掌",60,10,5),
    SkillData(102,"天龙八部",50,15,0),
    SkillData(103,"如来神掌",1,0,8),
    SkillData(104,"一阳指",10,1,9),
]
#1：获取敌人列表中，攻击力最小的敌人（内置高阶函数和listHelper实现）
result = min(list_skills,key=lambda e:e.atk)
print(result.name)
result01 =ListHelper.get_min(list_skills,lambda e:e.atk)
print(result01.name)
#2：根据血量对敌人列表进行降序排序
for i in sorted(list_skills,key=lambda e:e.cd,reverse=False):
    print(i.cd)

for i in ListHelper.order_by_descending(list_skills,lambda e:e.cd):
    print(i.cd)

for i in map(lambda e:e.name,list_skills):
    print(i)

for item in ListHelper.select(list_skills,lambda e:e.name):
    print(item.name)

#3：定义万能排序
def sort(target,func_condition):  #升序
    for i in range(len(target)-1):
        for y in range(i+1,len(target)):
            # if target[i] >target[y]:
            if func_condition(target[i],target[y]):#提取共性
                #相当于 def func(item01,item02):return item01>item02
                target[i],target[y] = target[y],target[i]
    return target
list01=[3,4,1,2]
print(sort(list01,lambda e1,e2:e1>e2))