
def input_student():
    L = []
    while True:
        name=input("输入学生姓名：")
        if not name:
            break
        age = int(input("输入学生年龄："))
        score = int(input("输入学生成绩："))
        d={
            'names':name,
            'ages':age,
            'scores':score
        }
        L.append(d)
    return L



def output_student(lst):
    stu_info = open('Stu_info', 'w', encoding='utf-8')
    for inf in lst:
        for i in inf:
            print(i,inf[i])
            stu_info.write(inf[i])
            stu_info.write(',')
            stu_info.close()
    print("+--------|--------|---------+")
    print("| name   |  age   |  score  |")
    print("+--------|--------|---------+")
    for d in lst:
        info="|%8s|%8d|%8d|"%(
            d['names'],d['ages'],d['scores']
        )
        print(info)
    print("+--------|--------|---------+")

L=input_student()
print(L)
output_student(L)


