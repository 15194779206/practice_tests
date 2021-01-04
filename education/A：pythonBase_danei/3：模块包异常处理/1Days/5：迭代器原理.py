'''迭代员工管理器对象'''

class Employee:
    pass
class EmployeeIterator:
    '''迭代器'''
    def __init__(self,target):
        self.target = target
        self.index = 0
    def __next__(self):
        if self.index >len(self.target)-1:
            raise StopIteration()
        item = self.target[self.index]
        self.index +=1
        return item

#可迭代对象
class EmployeeManager:
    def __init__(self,employee):
        self.all_employee = employee

    def __iter__(self): #返回迭代器
        return EmployeeIterator(self.all_employee)

manager = EmployeeManager([Employee(),Employee()])
for item in manager:
    print(item)

#和上面for循环一致
item = manager.__iter__()
while True:
    try:
        iterator = item.__next__()
        print(iterator)
    except StopIteration as e:
        break