#定义函数，选出所有女同学
class Student:
    def __init__(self, name, sex, age, score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
list_stu=[
    Student("张无忌", "男", 28, 83),
    Student("赵敏", "女", 20, 50),
    Student("周芷若", "女", 33, 60)
]

def selects():
    for item in list_stu:
        if item.sex =="女":
            yield item

for items in selects():
    print(items.name, items.sex, items.age, items.score)
