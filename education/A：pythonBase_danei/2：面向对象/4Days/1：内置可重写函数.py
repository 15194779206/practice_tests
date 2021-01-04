class StudentModel:
    """
     学生数据模型类
    """
    def __init__(self, name='', age=0, id=0):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return "我是%s,%s,%s"%(self.name,self.age,self.id)

    # def __repr__(self):
    #     return 'StudentModel(%s,%s,%s)'%(self.name,self.age,self.id)


s01 = StudentModel('lili','12','1')
# s02 = eval(s01.__repr__())
# print(s02)
print(s01)


class One:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "{}~{}".format(self.a,self.b)
    def __repr__(self):
        return "%d,%d"%(self.a,self.b)
one =One(1,2)
two=eval(one.__repr__())
#未添加__str__之前输出为<__main__.One object at 0x0000029FF1D6AA58>
print(one)   #1~2
print(two)#(1, 2)
























