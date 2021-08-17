'''
写一个student类，此类的对象有属性name ,age,secore
用来保存学生的姓名，年龄和成绩
 1)写一个函数input_student 读取n个学生的信息，用对象来存储这些信息
  (不用字典),并返回对象的列表
 2）写一个函数output_student()打印这些学生信息(格式不限)
'''
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def output_student(self):
        print(self.name, self.age, self.score)

def input_student():
    L = []
    while True:
        name = input('name:')
        if not name:
            break
        age = input('age:')
        score = input('score:')
        stu = Student(name,age,score)
        L.append(stu)
    return L



def main():
    L = input_student()
    for s in L:
        s.output_student()
main()