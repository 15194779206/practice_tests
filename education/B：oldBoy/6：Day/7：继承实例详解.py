#学校功能

class School(object):
    def __init__(self,addr,name):
        self.Name=name
        self.Addr=addr
        self.Student_list=[]
        self.Staff_list=[]
        self.course=[]
    def errol(self,stu_name):  #学生注册功能
        print(" %s 注册了安心家装饰"%stu_name.Name)
        self.Student_list.append(stu_name)
    def hire(self,tea_name):
        print("安心家装饰雇佣了 %s 老师"%tea_name.Name)
        self.Staff_list.append(tea_name)
    def creat_course(self):
        pass

#教师和学生公共类
class School_member():
    def __init__(self,name,age,sex):
        self.Name=name
        self.Age=age
        self.Sex=sex
    def tell(self):
        pass

#教师类
class Teather(School_member):
    def __init__(self,name,age,sex,salary,course):
        super(Teather,self).__init__(name,age,sex)
        self.Salary=salary
        self.Course=course
    def tell(self):
        print('''
        -----%s 的教师信息-----:
        name: %s
        age :%s
        sex:%s
        salary:%s
        course:%s
        '''%(self.Name,self.Name,self.Age,self.Sex,self.Salary,self.Course))
    def tell_course(self):
        print("%s 讲了 %s 课程，很动听"%(self.Name,self.Course))

#学生类
class Student(School_member):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.Stu_id=stu_id
        self.Grade=grade
    def tell(self):
        print('''
        -----%s 的学生信息-----:
        name: %s
        age :%s
        sex:%s
        salary:%s
        course:%s
        '''%(self.Name,self.Name,self.Age,self.Sex,self.Stu_id,self.Grade))
    def pay_tuition(self):
        print("%s 学生交了学费"%self.Name)

school=School("朝阳","嘉嘉乐")

t1=Teather("张",26,"男",15000,"自动化")
t2=Teather("刘",25,"女",16000,"性能")

s1=Student("小刘",30,"男",1801,"一班")
s2=Student("小张",22,"女",1802,"二班")

#方法的调用
school.errol(s1)  #注册
school.errol(s2)
school.hire(t1)  #交学费
school.hire(t2)

for stu in school.Student_list:
    stu.pay_tuition()

