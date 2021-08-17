'''
1：
以"万物皆对象'思想，洞察身边的事物，
创建两个类，2个对象
2：
创建学生类
    --数据：姓名，性别，年龄，成绩
    --行为：print_self()
  定义函数
    --在学生列表中，根据姓名查找学生对象
    --在学生列表中，根据性别查找所有学生对象
    --在学生列表中，查找年龄大于20，成绩大于60的所有学生对象
'''

class Student:
    def __init__(self,name='',sex='',age=0,score=0):
        self.name = name
        self.sex = sex
        self.age =age
        self.score = score

    def print_self(self):
        print("我叫%s,性别%s,今年%d岁,今年数学成绩为%d"%(self.name,self.sex,self.age,self.score))



stu1=Student("Alex",'男',20,30)
stu_list=[stu1,
          Student("judy","女",35,80),
          Student("Summer","女",35,50),
          Student("Blith","男",28,90)
          ]

def search_name(list,name):
    for lists in list:
        if lists.name == name:
            return lists

stu_first = search_name(stu_list,"Alex1")
if stu_first !=None:
    stu_first.print_self()
else:
    print("没有找到")



print("=="*20,"根据性别查找全部")
def search_sex(list,sex):
    lis = []
    for stu_info in list:
        if stu_info.sex ==sex:
            lis.append(stu_info)
    return lis

sea_sex =search_sex(stu_list,'男')
for i in sea_sex:
    if i ==None:
        print("没有找到")
    else:
        i.print_self()



print("=="*20,"age>20,score>60")
def search_ages(list,age,score):
    lis =[]
    for stu_info in list:
        if stu_info.age >age and stu_info.score >score:
            lis.append(stu_info)
    return lis

sec = search_ages(stu_list,20,60)
for info_li in sec:
    if info_li !=None:
        info_li.print_self()
    else:
        print("没找到")







'''
#创建两个类，狗类和猫类
class Dog:
    def __init__(self,name="",dog_type='',color=''):
        self.name = name
        self.dog_type = dog_type
        self.color = color

    def running(self):
        print("%s看见坏人就追"%self.name)

dog1=Dog("旺财",'哈士奇','red')
dog1.running()

class School:
    def __init__(self,address='',city=''):
        self.address = address
        self.city = city

    def include_tea(self,tea_name):
        print(tea_name)


sch01 =School("上海闵行区","上海")
sch01.include_tea("张老师")
'''




