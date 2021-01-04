diqiu={
    "北京":{
        "朝阳区":{
            "法院":"人民法院",
            "饭店":"和平饭店"
        },
        "海淀区":{
            "清河":"清河南镇",
            "大学":"科技大学"
        }
    },
    "上海":{
        "闵行区":{
            "第一个区":"不知道",
            "第二个区":"我哪知道"
        },
        "上海区":{
            "区域1":"上一",
            "区域2":"上二"
        }

    }
}
exit_flag=True

while exit_flag:
    for i in diqiu:
        print(i)
    choice=input("请输入省份：")
    if choice in diqiu:
        # print("\t",choice)
        while exit_flag:
            for i2 in diqiu[choice]:
                print("\t",i2)
            choice2=input("请输入市：")
            if choice2 in diqiu[choice]:
               while exit_flag:
                   for i3 in diqiu[choice][choice2]:
                       print(i3)
                   choice3 = input("请输入县：")
                   if choice3 in diqiu[choice][choice2]:
                       for i4 in diqiu[choice][choice2][choice3]:
                           print("\t",i4)
                       choice4 = input("最后一层：")
                       if choice4 == "b":
                           break
                       elif choice4=="e":
                           exit_flag=False
                   if choice3 =="b":
                        break
                   elif choice3 == "e":
                       exit_flag = False
            if choice2 == "b":
                break
            elif choice2 == "e":
                exit_flag = False