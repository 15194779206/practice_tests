'''
class StudentModel:
    """
     学生数据模型类
    """
    def __init__(self, name='', age=0, score=0, id=0):
        """
        创建学生对象
        :param id:  编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    @property
    def id(self):  #读属性
        return self.__id
    @id.setter
    def id(self,value):  #写入属性
        self.__id = value

    @property
    def name(self):
        return  self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        self.__score = value


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
        #自动生成
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

view = StudentManagerView()
con =StudentManagerController()

view.main()




# stu = StudentModel('zhangsan', 22, 80)
# controller= StudentManagerController()
# controller.add_student(stu)
# for y in controller.stu_list:
#     print(y.id, y.name, y.age, y.score)

'''

