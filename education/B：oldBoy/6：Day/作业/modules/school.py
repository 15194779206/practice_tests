import pickle
import  sys
import os
Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Dir)
from  database import data_cre
data_cre.data() #数据引入

# with open("teacher_dict.text",'rb') as f:
# datas=pickle.load(f)
class School():
    def __init__(self,sch_name,sch_addr):
        self.Sch_name=sch_name
        self.Sch_addr=sch_addr
        self.data__Course={}  #存储课程信息
    def cre_Course(self,obj_Course):
        print("%s 创建了 %s"%(self.Sch_name,obj_Course.Cour_name))
        self.data__Course.update({self.Sch_name:obj_Course.Cour_name})

class Course():
    def __init__(self,cour_name,zhouqi,price):#周期，价格
        self.Cour_name=cour_name
        self.Zhouqi=zhouqi
        self.Price=price
class Grade():
    pass

class Student():
    pass

class teacher():
    pass

course=Course('python','一年','10000')

school=School("beijing","chaoyang")
school.cre_Course(course)





























































































































































































