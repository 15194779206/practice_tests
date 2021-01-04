name=input("name:")
age=input("age:")
salary=input("salary:")
# 第一种语法打印输出
info='''
 ------- hello %s------
 Name:%s
 Age:%s
 salary:%s
'''%(name,name,age,salary)

# 第二种打印输出语句
info2='''
--------good {_name} ---------
Name={_name}
Age={_age}
Salary={_salary}
'''.format(_name=name,
           _age=age,
           _salary=salary,
       )

# 第三种打印输出语句
info3='''
--------world {0} ---------
Name={0}
Age={1}
Salary={2}
'''.format(name,age,salary)
# print(info3)

# 输入
nName=input("input your name:")
print("my name is"+nName)