class ModelMain:
    pass

class TeacherModel:
    pass

class TeacherManagerControllerr:
    pass

class TeacherManagerView:
    def __display_menu(self):
        menu = '''1)管理班级\n2)选择上课班级\n3)查看班级学员列表\n4)修改所管理学员成绩
        '''
        print(menu)

    def manageClass(self):  # 管理班级
        print("manageClass")

    def selectTeachClass(self):  # 选择上课班级
        print('selectTeachClass')

    def classStudentList(self):  # 查看班级学员列表
        print("classStudentList")

    def modifyScore(self):  # 修改所管理学员成绩
        print("modifyScore")

    def __select_menu(self):
        number = input("select input：")
        if number == "1":
            self.manageClass()
        elif number == "2":
            self.selectTeachClass()
        elif number == "3":
            self.classStudentList()
        elif number == "4":
            self.modifyScore()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()