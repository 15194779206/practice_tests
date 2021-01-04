class ModelMain:
    pass

class  ManagementModel:
    pass

class  ManagementManagerControllerr:
    def __init__(self):
        self.school_list = []
    def  createSchoolCon(self,school):
        self.school_list.append(school)
        for i in self.school_list:
            print(i)

class  ManagementManagerView:
    def __init__(self):
        self.manageCon = ManagementManagerControllerr()
    def __display_menu(self):
        menu = '''1)创建讲师\n2)创建班级\n3)创建课程\n4)创建学校
        '''
        print(menu)

    def createTeacher(self):  # 创建讲师
        print("createTeacher")

    def createClass(self):  # 创建班级
        print('createClass')

    def createCourse(self):  # 创建课程
        print("createCourse")

    def createSchool(self):  # 创建学校
        createSchool = input("请输入学校名:")
        self.manageCon.createSchoolCon(createSchool)


    def __select_menu(self):
        number = input("select input：")
        if number == "1":
            self.createTeacher()
        elif number == "2":
            self.createClass()
        elif number == "3":
            self.createCourse()
        elif number == "4":
            self.createSchool()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

if __name__ == '__main__':
    view = ManagementManagerView()
    view.main()