#逻辑上的判断建立在此基础上
#学校类,  属性--学校地址；方法--
def con():
    print("lala")

class School(object):
    def __init__(self,sch_name,sch_addr):
        self.Sch_name=sch_name
        self.Sch_addr=sch_addr
        self.Sch_send_view=[]
        self.Stu_send_view=[]
        self.Tea_send_view=[]
    #哪个学校创建了课程
    def start_Men(self,obj_cour):
        print("%s 创建了 《%s》课程"%(self.Sch_name,obj_cour.Cour_name))
    #学校创建班级
    def Sch_new_class(self,obj_class):
        print("%s 创建了 %s班级"%(self.Sch_name,obj_class.Class_ban))
    #学员注册添加
    def enroll(self,obj_tudent):# 学员注册
        # self.Stu_send_view.append(obj_tudent)
        print("%s 学生注册的地址是 %s "% (obj_tudent.name, self.name))

#课程是学校子类，调用学校类== 属性--课程名称，周期，价格，方法--课程在哪开，学校存储数据
class Course(School):
    def __init__(self,sch_name,sch_addr,cour_name,zhouqi,cour_price):
        super(Course,self).__init__(sch_name,sch_addr)
        self.Cour_name=cour_name
        self.Zhouqi=zhouqi
        self.Cour_price=cour_price
    def CourInfo(self):
        print('''-----[%s]课程信息-----
        学校地址：%s
        学校信息:%s
        课程名称：%s
        课程周期：%s
        课程价格：%s
        '''%(self.Cour_name,self.Sch_name,self.Sch_addr,self.Cour_name,self.Zhouqi,self.Cour_price))
    #学生交费

    #班级关联课程
    # def class_cour(self,obj_classroom):
    #     print("%s 班级选择了 [%s]"%(self.Cour_name,obj_classroom.))

#创建班级类，通过学校创建班级
class Classroom(School):
    def __init__(self,sch_name,sch_addr,banji):
        super(Classroom,self).__init__(sch_name,sch_addr)
        self.Class_ban=banji
    #学员关联班级

#创建学生类
class Student(School):
    def __init__(self,sch_name,sch_addr,stu_name):
        super(Student,self).__init__(sch_name,sch_addr)
        self.Stu_name=stu_name

#创建老师类




















#
# s1=School("北京","沙河")
# c1=Course("上海","闵行区","linux","6个月",3000)
# classr=Classroom("天津","海湾","一班")
# s1.start_Men(c1)
# c1.CourInfo()
# s1.Sch_new_class(classr)




#课程类，课程和学校绑定--学校写单独的接口



#学校视图   创建班级，讲师，课程
#讲师视图   查看班级，查看班级学员列表
#学生视图   注册时选择学校，选择班级，报名缴费，
