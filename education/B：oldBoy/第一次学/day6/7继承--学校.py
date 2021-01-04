#要求，学校可以统计多少个学员，学校包括注册方法
#学校 :属性---姓名和地址：：方法---学员注册enroll，雇佣新员工hire

import pickle

class School(object):
    def __init__(self,name,addr):
        self.Name=name
        self.Addr=addr
        self.Student=[]   #创建一个学生的元组用来接收学生姓名
        self.Teacher=[]   #创建一个元组用来接收老师信息
    def enroll(self,obj_stuName):
        print("%s 学校为 %s 办理入学"%(self.Name,obj_stuName.Name))
        self.Student.append(obj_stuName)   #获取到的学员放在Student里面
    def hire(self,obj_teaName):
        print("%s 雇佣 %s 老师"%(self.Name,obj_teaName.Name))
        self.Teacher.append(obj_teaName)

#学校成员：摘取学生和老师的公共，到时直接调用
class SchoolMember():
    def __init__(self,name,age,sex):
        self.Name=name
        self.Age=age
        self.Sex=sex
#老师：属性---姓名，年龄，性别，工资，课程：：方法--教课程
class  Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.Salary=salary
        self.Course=course
    def teacherInfo(self):
        print('''------%s的信息------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.Name,self.Name,self.Age,self.Sex,self.Salary,self.Course))
    def teach_con(self):
        print("%s 老师教[%s]课程"%(self.Name,self.Course))

#学生：属性---姓名，年龄，性别，stu_id，班级：：方法--交学费
class  Student(SchoolMember):
    def __init__(self,name,age,sex,stuid,classroom):
        super(Student,self).__init__(name,age,sex)
        self.Stu_id=stuid
        self.Classroom=classroom
    def studentInfo(self):
        print('''------学生：{_name} 的信息-----
        Name:{_name}
        Age:{_age}
        Sex:{_sex}
        StuId:{_stuid}
        Classroom:{_classroom}
        '''.format(_name=self.Name,
                   _age=self.Age,
                   _sex=self.Sex,
                   _stuid=self.Stu_id,
                   _classroom=self.Classroom)
        )
    def payMoney(self,pay_count):
        print("%s 交 学费 $%s"%(self.Name,pay_count))



#学校信息
school=School("北京老男孩","北京沙河")

#打印教师信息
t1=Teacher("刘宏伟",22,"男",3000,"物理")
t2=Teacher("李伟",25,"女",5000,"化学")
t1.teacherInfo()
t1.teach_con()

#打印学生信息
s1=Student("晓强",22,"男","22号","一年级")
s2=Student("张三",20,"女","01号","二年级")
s1.studentInfo()
# s1.payMoney(5000)


#学校方法的调用
school.enroll(s1)
school.enroll(s2)
school.hire(t1)

#调用学校中的学生姓名，调用学生类中的paymney方法
for stu in school.Student:
    stu.payMoney(5000)
"""
#序列化存入内容
# print((school.Student))
# f=open("test.text",'r+',encoding="utf-8")
# pickle.dumps(school.Student,f)

#执行程序
def zhuce():
    New_name=input("请输入姓名：")
    tianjia=school.Student
    print(tianjia)
    if New_name in tianjia:
        print("您已进行注册，是否直接选择班级？")
        resq=input("1:Y\n2:N\n")
        if resq=="Y":
            print("此功能未做")
        else:
            print("此功能未做")
    else:
        print("lal")



def jiaoxuefei():
    pass
def ChooseClass():
    pass
def Stu_Info():
    pass

#启动运行
def run():
    print("="*10+"学生视图"+"="*10)
    while True:
        print("1:注册\n2:交学费\n3:选择班级\n4:查看信息\n")
        # 此处出现了一个错误，将input不小心写成了print，陷入了死循环
        con = input("请选择要操作的程序:")
        if con == "1":
            zhuce()
        elif con == "2":
            jiaoxuefei()
        elif con == "3":
            ChooseClass()
        elif con == "4":
            Stu_Info()
        else:
            print("输入序号不正确，请重新进行选择")

run()

"""
