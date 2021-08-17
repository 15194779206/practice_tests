username="alex"
password="22"
name=input("Name:")
passw=input("pass:")
if username==name and password==passw:
    print("welecome {_name} come here".format(_name=name))
else:
    print("not true")


# 多个循环
oldage=56;
   # 因为input默认输入类型为str，两种类型不可进行比较，所以出现错误
age=int(input("age:"))
if oldage==age:
    print("you are right")
elif oldage>age:
    print("down age")
else:
    print("up age")