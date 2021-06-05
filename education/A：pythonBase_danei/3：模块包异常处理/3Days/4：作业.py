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

def searchs(lists,funs):
    for item in lists:
        if funs(item):
            yield item

# def fun01(item):
#     return item.id==0

def prints(info,item):
    print(info,item.id,item.name,item.atk,item.cd,item.costSP)

#查找所有血量为0的对象
for item in searchs(list_skills,lambda items:items.cd==0):
    prints("血量等于0",item)


#查找所有血量大于0 的对象
for item in searchs(list_skills,lambda item:item.cd>0):
    prints("血量大于0",item)

#查找攻击速度大于5的对象
for item in searchs(list_skills,lambda item:item.atk>5):
    prints("攻击速度大于5",item)

#查找所有攻击速度在5-10之间的敌人
for item in searchs(list_skills,lambda item:item.atk>5 and item.atk<=10):
    prints("攻击速度大于5小于10",item)

#查找编号为101的对象
for item in searchs(list_skills,lambda item:item.id ==101):
    prints("编号为101:",item)

#查找所有敌人的姓名
def search01(lists,funs):
    for item in lists:
        yield funs(item)

for item in search01(list_skills,lambda item:item.name):
    print("allname",item)


#获取满足条件的最后一个对象
def find_demo01(target,func):
    for i in range(len(target)-1,-1,-1):
        # if target[i].hp>0:
        if func(target[i]):
            return target[i]

    #提取
def func(item):
    return item.cd>0

    #获取最后一个活人

result = find_demo01(list_skills,lambda e:e.cd>0)
print(result.name)


    #获取攻击速度大于5的最后一个敌人


#获取具有生命值对象总数
def find_demo02(target,func):
    index =0
    for item  in target:
        # if item.cd>0:
        if func(item):
            index+=1
    return index

result02=find_demo02(list_skills,lambda e:e.cd>0)
print(result02)



#判断列表中是否含有死人
def find_demo03(target,func):
    for item in target:
        # if item.cd==0:
        if func(item):
            return True
    return False

result03 = find_demo03(list_skills,lambda e:e.cd==0)
if result03:
    print("含有死人")
else:
    print("不含有")



#删除所有死人
def find_demo04(target,func):
    del_count = 0
    for item in range(len(target)-1,-1,-1):
        # if target[item].cd==0:
        if func(target[item]):
            del target[item]
            del_count+=1
    return del_count

#删除编号为101的敌人

# result04=find_demo04(list_skills,lambda e:e.cd ==0)
# print(result04)
# for i in list_skills: #查看剩下的人数
#     print(i.name)

print("*"*50)

#获取血量最大的敌人
def find_demo05(target,func):
    max_value = target[0]
    for i in range(1,len(target),1):
        # if max_value.cd <target[i].cd:
        if func(max_value) <func(target[i]):
            max_value = target[i]
    return max_value
    #代码提取
def fun01(item):
    return item.cd

result05 = find_demo05(list_skills,lambda e:e.cd)
print(result05.name)


#根据血量升序排列
def find_demo06(target,func):
    for i in range(len(target)-1):
        for y in range(i+1,len(target)):
            # if target[i].cd >target[y].cd:
            if func(target[i]) >func(target[y]):
                target[i],target[y] = target[y],target[i]
    return target
    #提取变化点
def func(item):
    return item.cd

result06 = find_demo06(list_skills,lambda e:e.cd)
for item in result06:
    print(item.name,item.cd)







