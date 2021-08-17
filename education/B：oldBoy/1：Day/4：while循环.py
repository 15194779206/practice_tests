
#while循环模块
Age=56
count=0
while count<3:
    age=int(input("请输入年龄："))
    print("count:",count)
    if age==Age:
        print("输入正确")
        break
    elif age>Age:
        print("输入过大")
    else:
        print("输入过小")
    count+=1
    if count==3:
        pardent=input("是否继续：")
        if pardent!='n':
            count=0
#如果上面有循环条件，上面不存在if也是可以的
else:
    print("输入次数过多")