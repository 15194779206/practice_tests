name ='alex'
age=22
def Login():
    count = 0
    while count < 3:
        names = input("请输入您的用户名：")
        ages = input("请输入您的年龄：")
        if names == 'alex' and ages == '22':
            print("登录成功")
            break
        else:
            print("登录失败")
        count += 1
    else:
        print("您已连续错误三次，禁止登录")


Login()