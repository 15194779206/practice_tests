from list_tools import *
new_list=[
    {'id':1,'name':"zhangsan",'age':18,'score':100,'cd':100},
    {'id':2,'name':"lisi",'age':22,'score':33,'cd':80},
    {'id':3,'name':"wangwu",'age':10,'score':110,'cd':100},
    {'id':4,'name':"zhaoliu",'age':13,'score':60,'cd':100},
    ]
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
    SkillData(104,"一阳指",50,1,9),
]
# 1：降序排序
# for r in range(len(new_list) - 1):
#     for c in range(r + 1, len(new_list)):
#         if new_list[r]['score'] < new_list[c]['score']:
#             new_list[r], new_list[c] = new_list[c], new_list[r]
# print(new_list)
# # 2：获取所有的姓名
# for item in ListHelper.find_all(list_skills,lambda e:e.id>101):
#     print(item.id)
# result =ListHelper.first(list_skills,lambda e:e.atk==50)
# print(item.name)

result =ListHelper.count(list_skills,lambda e:e.atk)
print(result)

# for item in ListHelper.select(list_skills,lambda e:e.atk>40):
#     print(item)


def select(list_stu,func_condition):
    for item in list_stu:
        yield func_condition(item)

def func(e):
    return e.atk>10
for i in select(list_skills,func):
    print(i)
# 3：获取年龄大于15的最后一名人员

# 4：获取分数总数

# 5：判断是否有不合格人员(score<=70)
#
# 6：删除所有分数小于等于70的人员

# 7：获取分数值最大的员工
