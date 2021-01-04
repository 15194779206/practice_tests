import education


def add_Banji():
    print("===创建班级===")
    name_banji=input("请输入班级名称：")


def add_Tea():
    pass
def add_Cour():
    pass
def add_School():
    print("请填写学校信息：")
    school_name = input("名称：")
    address = input("地址：")

    school = education.School(school_name, address)
    print(school)

def run():
    print("学生视图：")
    print("=" * 20)
    while True:
        print("1.创建班级\n2.创建讲师\n3.创建课程\n4.创建学校\n")
        res = input("输入序号：")
        if res == "1":
            add_Banji()
        elif res == "2":
            add_Tea()
        elif res == "3":
            add_Cour()
        elif res == "4":
            add_School()
        else:
            print("请选择正确的编号")

run()
