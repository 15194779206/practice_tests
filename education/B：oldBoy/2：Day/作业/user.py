"""
购物车程序
   用户入口：
      1.商品信息存在文件里
      2.已购商品，余额记录。
   商家入口：
      1.可以添加商品，修改商品价格
"""
import time
import os,sys

#用户名列表的判断操作
User=open("user_list",'r',encoding="utf-8")
user_list=User.readlines()
#商品列表
Shop_list = open('Shop_list', 'r', encoding='utf-8')


print("用户操作："
      "1：我是用户"
      "2：我是商家")
user_choose=input("请选择用户角色：")
if user_choose=='1':
    user_name = input("请输入用户名：")
    #判断锁定用户
    Clock_user = open("clock_user", 'r', encoding='utf-8')
    clo_user=Clock_user.readlines()
    for clock_user in clo_user:
        if user_name == clock_user.strip():
            print("用户已锁定")
            sys.exit()
    for user in user_list:
        user_na = user.split(",")[0].strip()
        user_pa = user.split(",")[1].strip()
        if user_name == user_na:
            i = 0
            while i < 3:
                passw = input("请输入密码：")
                if passw == user_pa:
                    print("欢迎%s进入，请选择要操作的内容:\n"
                          "1：打印商品列表"
                          "2：查看余额信息" % user_na)
                    user_do=input("用户操作：")
                    if user_do=='1':
                        print("shangpin")

                    elif user_do=='2':
                        print("用户列表")
                    else:
                        print("无此功能")
                else:
                    if i != 2:
                        print("还有%s机会" % (2 - i))
                i += 1
            else:
                fal_txt = open("clock_user", 'r+', encoding="utf-8")
                fal_txt.write(user_na)
                sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % user_na)
        else:
            print("用户不存在")



elif user_choose=='2':
    user_cho=input("用户操作："
                   "1：添加商品"
                   "2：修改商品价格")
    if user_cho=='1':
        pass
    elif user_cho=='2':
        for line in Shop_list.readlines():
            curline = line.strip().split(' ')
            # print(curline)
            for i,index in enumerate(curline):
                # print(i)
                print([index])
    else:
        print("无此操作，并退出")
else:
    print("输入错误，请明确后重新输入")
