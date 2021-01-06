class StudentManagerController:
    '''
     数据：学生列表  __stu_list
        行为：获取列表只读  stu_list
             添加学生方法  add_student
             删除学生   remove_student
             修改学生  update_student
    '''
    pass

class StudentModel:
    # 数据：编号id(自动生成)  姓名name   年龄age  成绩 score ---->用属性进行保护
    def __init__(self,id=0,name='',age =0,score=0):
        self.id =id
        self.name =name
        self.age =age
        self.score = score


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
    pass