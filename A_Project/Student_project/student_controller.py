'''
class StudentManagerController:
    """
    学生逻辑控制器
    """
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self): #做成只读属性
        return self.__stu_list

    def add_student(self, stu):
        stu.id =self.__generate_id()
        self.__stu_list.append(stu)


    def __generate_id(self):

        # :return:id 自动生成

        if len(self.__stu_list) >0:
            id = self.__stu_list[-1].id+1
        else:
            id = 1
        return id
    def order_by_score(self):  #程序排序
        #创建新列表：目的--不影响原有列表
        new_list = self.__stu_list[:]
        for r in range(len(new_list)-1):
            for c in range(r+1,len(new_list)):
                if new_list[r].score >new_list[c].score:
                    new_list[r],new_list[c] =new_list[c],new_list[r]
        return new_list

    def remove_student(self, id):
        """
        删除学生
        :param id:
        :return:
        """
        for item in self.stu_list:
            if item.id ==id:
                self.stu_list.remove(item)
                return True
        return False

    def update_student(self,stu):
        """
        修改学生信息
        :return:
        """
        for item in self.stu_list:
            if item.id ==stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False
'''

from A_Project.Student_project.student_model import *
class StudentManagerController:
    def __init__(self):
        self.__stu_list = []  #学生列表
        # self.mo = StudentModel()

    @property
    def stu_list(self): #获取列表的只读属性
        return self.__stu_list

    def __generate_id(self):
        """
        编号生成
        :return:自增id
        """
        # if len(self.__stu_list) == 0:
        #     id = 1
        # else:
        #     id = self.__stu_list[-1].id + 1
        # return id
        #或是可以简化写
        return 1 if len(self.__stu_list) == 0 else self.__stu_list[-1].id + 1

    def add_student(self, stu): #添加学生方法
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)


    def remove_student(self,id): #删除学生
        for items in self.stu_list:
            if items.id == id:
                self.stu_list.remove(items)
                return True
        return False
            #     print("删除成功")
            # else:
            #     print("删除失败")

    def update_student(self,id): #修改学生
        for stuID in self.stu_list:
            if id in stuID:
                print("cunzai")
            else:
                print("不存在")

    def order_by_score(self): #根据成绩排序
        list_stu = self.__stu_list[:]#形成新的列表不对原列表操作
        for x in range(len(list_stu)-1):
            for y in range(x+1,len(list_stu)):
                if list_stu[x].score > list_stu[y].score:
                    list_stu[x],list_stu[y] =list_stu[y],list_stu[x]
        return list_stu
        #错误思想
        # for item in self.__stu_list[:]:
        #     if item[0].score > item[1].score:
        #         item[0],item[1] = item[1],item[0]


# c1 = StudentManagerController()
# c1.add_student(StudentModel('zs',11,80))
# c1.add_student(StudentModel('ls',15,90))
# for i in c1.stu_list:
#     print(i.id,i.name,i.age,i.score)


