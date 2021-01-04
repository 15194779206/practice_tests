
#输入姓名和年龄，进行判断
Name="张三"
Age=23  #此处输入默认为字符串
name=input("请输入姓名：")
age=int(input("请输入年龄："))
if Name==name and Age==age:
    print("输入正确")
elif Name!=name or Age!=age:
    print("用户名或密码错误")
else:
    print("请重新输入")
