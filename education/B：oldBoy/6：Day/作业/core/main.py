import sys


def run():
    print("请输入用户角色："
          "1：学校视图"
          "2：教师视图"
          "3：学生视图")
    user_choose=input("请输入要登录的视图：")
    if user_choose=='1':
        Manage_view()
    elif user_choose =='2':
        Teacher_view()
    elif user_choose == '3':
        Student_view()
    elif user_choose == 'q':
        sys.exit()
    else:
        print("视图不存在，请重新输入")

class Manage_view():
    pass

class Teacher_view():
    pass

class Student_view():
    pass

