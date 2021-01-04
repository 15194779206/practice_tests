import sys

Username=input("请输入用户名：")
clock_file=open("account_lock.txt",'r+')
clock=clock_file.readlines()
#判断用户锁定状态
for clock_na in clock:
    clock_na=clock_na.strip('\n')
    if clock_na == Username:
        sys.exit('%s 用户处于锁定状态，退出'%Username)
#判断用户是否存在
account=open('account.txt','r',encoding='utf-8')
acc_file=account.readlines()
for acc_info in acc_file:
    acc_info=acc_info.strip('\n')
    (user,password)=acc_info.split()  #按照空格进行分隔
    if Username == user:
        j=0
        while j<3:
            Password=input("请输入密码：")
            if Password ==password:
                sys.exit("%s 欢迎进入，登录成功"%Username)
            else:
                print("您已错误 %s 次"%(j+1))
            j+=1
        else:
            clock_file.write('\n'+Username)
            sys.exit("强制退出并锁定")
    else:
        pass
else:
    sys.exit("%s 用户不存在"%Username)

clock_file.close()
account.close()






