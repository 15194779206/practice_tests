class StudentModel:
    def __init__(self, name='', age=''):
        self.name = name
        self.age = age

class StudentManagerController:
    def __init__(self):
        self.__stu_list = []


    def studentRegister(self,stu):
        self.__stu_list.append(stu)
        # for item in self.__stu_list:
        #     if item.name == stu.name:
        #         print("已存在")

    def studentpayTuition(self):
        pass

    def studentselectClass(self):
        pass

class StudentManagerView:
    def __init__(self):
        self.stucontroller = StudentManagerController()

    def __display_menu(self):
        menu ='''1)注册\n2)交学费\n3)选择班级
        '''
        print(menu)
    def register(self): #注册
        stuModel = StudentModel()
        stuModel.name = input('name:')
        stuModel.age = input('age:')
        self.stucontroller.studentRegister(stuModel)

    def payTuition(self):  #交学费
        print('pay')

    def selectClass(self): #选择班级
        print("select")

    def __select_menu(self):
        number = input("select input：")
        if number == "1":
            self.register()
        elif number == "2":
            self.payTuition()
        elif number == "3":
            self.selectClass()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

if __name__ == '__main__':
    stuview = StudentManagerView()
    stuview.main()


