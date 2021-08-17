# 作业二：编写登陆接口
#     输入用户名密码
#     认证成功后显示欢迎信息
#     输错三次后锁定

#存在的问题，用户不存在无法判断
import os
import sys

count=0
name = input("请输入姓名：")
False_f = open("False_inform", "r", encoding="utf-8")
Lock_list=False_f.readlines()
for line in Lock_list:
    List = line.strip()
    if name==List:
        sys.exit("%s已被锁定,退出"%name)
user_name = open("True_inform", 'r', encoding="utf-8")
user_list=user_name.readlines()
for user_line in user_list:
    (user,password)=user_line.strip().split(" ")
    # print(user,password)
    if name==user:
        i=0
        while i<3:
            passw=input("请输入密码：")
            if passw==password:
                print("欢迎%s进入"%name)
                sys.exit(0)
            else:
                if i!=2:
                    print("还有%s机会"%(2-i))
            i+=1
        else:
            fal_txt = open("false_inform", 'w', encoding="utf-8")
            fal_txt.write(name)
            sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % name)
    else:
        print("用户不存在")
        # sys.exit(0)
False_f.close()
user_name.close()













