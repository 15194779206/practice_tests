class StudentModel:
    # 数据：编号id(自动生成)  姓名name   年龄age  成绩 score ---->用属性进行保护
    def __init__(self,id=0,name='',age =0,score=0):
        self.id =id
        self.name =name
        self.age =age
        self.score = score


class StudentManagerController:
    '''
     数据：学生列表  __stu_list
        行为：获取列表只读  stu_list
             添加学生方法  add_student
             删除学生   remove_student
             修改学生  update_student
    '''

    def __init__(self):
        self.__stu_list=[]

    def stu_list(self):
        pass

    def add_student(self):
        pass

    def remove_student(self):
        pass

    def update_student(self):
        pass

class StudentManagerView:
    '''
    数据：逻辑控制对象  __manager =  StudentManagerController()
        行为：显示菜单   __display_menu ,
             选择菜单项 __select_menu
             输入学生  __input_students
             输出学生  __output_students
             删除学生  __delete_students
             修改学生信息  __modify_student
             按成绩输出学生   __output_student_by_score
             入口逻辑  main
    '''
    def __display_menu(self):
        meun='''
     1)添加学生信息
     2)显示所有学生信息
     3)删除学生信息
     4)修改学生成绩
     5)按学生成绩低-高显示学生信息
     6)按学生成绩高-低显示学生信息
     7)按学生年龄高-低显示学生信息
     8)按学生年龄低-高显示学生信息
     q)退出
        '''
        print(meun)
    def __select_menu(self):
        selects = input("请输入操作：")
        if selects == '1':
            self.__input_students()
        elif selects == '2':
            self.__output_students()
        elif selects == '3':
            self.__delete_students()
        elif selects == '4':
            self.__output_students()

    def __input_students(self):
        print("select")

    def __output_students(self):
        pass

    def __delete_students(self):
        pass

    def __modify_students(self):
        pass

    def __output_student_by_score(self):
        pass

    def main(self):
        self.__display_menu()
        self.__select_menu()




if __name__ == '__main__':
    view = StudentManagerView()
    view.main()























