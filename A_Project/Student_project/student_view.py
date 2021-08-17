'''
from A_Project.Student_project.student_controller import *
from A_Project.Student_project.student_model import *

# 3：界面视图类  StudentManagerView
class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    def __input_students(self): #输入学生
        stu =StudentModel()
        stu.name = input("name:")
        stu.age = int(input("age:"))
        stu.score = int(input("score:"))
        self.__manager.add_student(stu)
            # if stu.name == "exit":
            #     break

    def __output_students(self,target_list):#显示学生列表
        # for stu in self.__manager.stu_list:
        for stu in target_list:
            print("%d-%s-%d-%d"%(stu.id,stu.name,stu.age,stu.score))


    def __output_student_by_score(self):
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __delete_students(self):
        input_id = int(input("请输入学生编号:"))
        if self.__manager.remove_student(input_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu =StudentModel()
        stu.id = int(input("id:"))
        stu.name = input("name:")
        stu.age = input("age:")
        stu.score = input("score:")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("更新失败")


    def __display_menu(self):
        print(" 1)添加学生信息\n",
              "2)显示所有学生信息\n",
              "3)删除学生信息\n",
              "4)修改学生成绩\n",
              "5)按学生成绩低-高显示学生信息\n")

    def __select_menu(self):
        number = input("请输入选项：")
        if number =="1":
            self.__input_students()
        elif number == "2":
            self.__output_students(self.__manager.stu_list)
        elif number =="3":
            self.__delete_students()
        elif number =="4":
            self.__modify_student()
        elif number =="5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

'''
from A_Project.Student_project.student_controller import *
from A_Project.Student_project.student_model import *
class StudentManagerView:
    def __init__(self):
        self.__manager =  StudentManagerController()

    def __display_menu(self):  #显示菜单
        menu = '''
        1)添加学生
        2)显示所有学生
        3)删除学生
        4)修改学生成绩
        5)按学生成绩低-高显示学生信息
        6)按学生成绩高-低显示学生信息
        7)按学生年龄高-低显示学生信息
        8)按学生年龄低-高显示学生信息
        q)退出
        '''
        print(menu)
    def __input_int(self,msg):
        while True:
            try:
                return int(input(msg))
            except Exception as e:
                print("输入有误")

    def __input_students(self): #输入学生
        stu = StudentModel()
        stu.name = input("name:")
        # while True:  #这样写代码重复率太高
        #     try:
        #         stu.age = int(input("age:"))
        #     except Exception as e:
        #         print("年龄有误")
        # stu.age = int(input("age:"))
        stu.score = input("score:")
        stu.age = self.__input_int("age:")
        stu.score = self.__input_int("score:")
        self.__manager.add_student(stu)

    def __output_students(self,lists):  #输出学生
        for item in lists:
            print(item.id, item.name, item.age, item.score)

    def __delete_students(self):  #删除学生
        self.__output_students(self.__manager.stu_list)
        id = int(input("输入删除id："))
        self.__manager.remove_student(id)
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self): #修改学生信息
        self.__output_students(self.__manager.stu_list)
        id = int(input("请输入修改学生ID："))
        self.__manager.update_student(id)


    def __output_student_by_score(self): #按成绩输出学生
        target_list = self.__manager.order_by_score()
        self.__output_students(target_list)

    def __select_menu(self):  #选择菜单项
        selects = input("请输入选择项：")
        if selects == "1":
            self.__input_students()
        if selects == "2":
            self.__output_students(self.__manager.stu_list)
        if selects == "3":
            self.__delete_students()
        if selects == "4":
            self.__modify_student()
        if selects == "5":
            self.__output_student_by_score()
        if selects == "q":
            exit()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

s1=StudentManagerView()
s1.main()
