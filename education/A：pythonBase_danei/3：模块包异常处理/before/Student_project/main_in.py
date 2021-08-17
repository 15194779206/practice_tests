import stu_info
def show_menu():
    print("1)添加学生信息\n"
          "2)显示所有学生信息\n"
          "3)删除学生信息\n"
          "4)修改学生成绩\n"
          "5)按学生成绩高-低显示学生信息\n"
          "6)按学生成绩低-高显示学生信息\n"
          "7)按学生年龄高-低显示学生信息\n"
          "8)按学生年龄低-高显示学生信息\n"
          "q)退出")

def delete_info(lis):
    print(lis)
    cho=input("请输入要删除学生姓名：")

def revise_info():
    pass
def score_high(info):
    info_age = info[:]
    foo = lambda s: s['scores']
    info.sort(key=foo)
    items = sorted(info_age, key=foo,reverse=True)
    print(items)
def score_low(info):
    info_age = info[:]
    foo = lambda s: s['scores']
    info.sort(key=foo)
    items = sorted(info_age, key=foo)
    print(items)
def age_high(info):
    info_age = info[:]
    foo = lambda s: s['arges']
    info.sort(key=foo)
    items = sorted(info_age, key=foo, reverse=True)
    print(items)
def age_low():
    pass

def main():
    docs=[]
    while True:
        show_menu()
        recode = input("请输入要操作的界面：")
        if recode=='q':
            return print("欢迎您再次进入")
        if recode == '1': #添加
            docs+=stu_info.input_student()
        elif recode =='2': #显示
            stu_info.output_student(docs)
        elif recode =='3': #删除
            delete_info(docs)
        elif recode =='4': #修改
            pass
        elif recode =='5':
            pass
        elif recode =='6':
            score_low(docs)
        elif recode =='7':
            pass
        elif recode =='8':
            pass

if __name__ == '__main__':
    main()