class Employee:
    pass
class EmployeeManager:
    def __init__(self,employees):
        self.all_employees =employees

manager = EmployeeManager([Employee(),Employee()])

for item in manager:
    print(item)