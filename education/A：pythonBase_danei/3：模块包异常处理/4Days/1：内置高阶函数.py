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
def func(e):
    if e.atk>50:
        return e
          #func可以写成 lambda e:e.atk>50
for item in filter(func, list_skills):  #根据条件获取
    print(item.name)
for item in map(lambda e:e.name,list_skills): #输出所有姓名
    print(item)
for item in sorted(list_skills,key=lambda e:e.atk): #按照攻击力升序排序
    print(item.atk)
result = max(list_skills,key=lambda e:e.atk) #找出攻击力最大值
print(result.atk)


print("*"*50)
#查找血量在10-15之间的敌人
for item in filter(lambda e:e.atk>=10 and e.atk<=100,list_skills):
    print(item.name)
#查找所有敌人的攻击力
for item in map(lambda e:e.atk,list_skills):
    print("map",item)
#根据攻击力对敌人进行升序排序

for item in sorted(list_skills,key=lambda e:e.atk):
    print("攻击力排序",item.atk)

result02=max(list_skills,key=lambda e:e.name)
print(result02.name)









