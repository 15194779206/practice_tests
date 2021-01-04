uname="zhang"
upass="123"
count=0
while count<3:
    name=input("请输入用户名：")
    passwd=input("亲输入密码：")
    if uname==name and upass==passwd:
        print("welecome you come here")
        break
    else:
        print("username or pass error")
    count+=1
    if count==3:
        cont=print("是否还要继续？")
        if cont!='n':
            count=0
