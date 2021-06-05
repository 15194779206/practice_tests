
'''
注释的内容
'''
#第一种输出语句
name=input("请输入姓名：")
#默认输入为str,如果想要字符串，需要进行转换
salary=int(input("请输入工资："))
work=input("请输入职位：")
inform='''
------用户名：%s------
Name:%s
Salary:%d
Work:%s
'''%(name,name,salary,work)
print(inform)

#第二种输出语句
inform2='''
------用户名2：{_name}------
Name:{_name}
Salary:{_salary}
Work:{_work}
'''.format(_name=name,_salary=salary,_work=work)

print(inform2)

