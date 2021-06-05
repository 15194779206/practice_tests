'''
2：完成学生管理系统，修改学生信息

3：一家公司，有如下几个岗位：
    普通员工：底薪
    程序员：底薪+项目分红
    销售员：底薪+销售额
  定义员工管理器，记录所有员工，提供计算总薪资方法
  要求：增加新岗位，员工管理器代码不做修改
体会：依赖倒置
'''


class StaffManager:
    def __init__(self):
        self.__staffList=[]

    def add_staff(self,g):
        self.__staffList.append(g)

    def total_salary(self):
        total_salary =0
        for lists in self.__staffList:
            total_salary += lists.baseSalary()
        print(total_salary)


class Staff:
    """员工类"""
    def __init__(self,salary):
        self.base_salary = salary

    def baseSalary(self):
        return self.base_salary



class BasicStaff(Staff):
    pass

class ITstaff(Staff):
    def __init__(self,fenhong,base_salary):
        super().__init__(base_salary)
        self.fenhong=fenhong

    def baseSalary(self):
        return super().baseSalary()+self.fenhong


class Salestaff(Staff):
    def __init__(self, project_money, base_salary):
        super().__init__(base_salary)
        self.project_money = project_money

    def baseSalary(self):
        return super().baseSalary() + self.project_money*0.05


b01 =ITstaff(10,2)
st01 =StaffManager()
st01.add_staff(b01)
st01.total_salary()























