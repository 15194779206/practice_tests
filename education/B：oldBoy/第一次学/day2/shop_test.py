Shop_list=[
    ("苹果",2000),
    ("香蕉",3000),
    ("鸭梨",4000),
    ("桃子",5000)
]
# 选择的商品存在一个列表中
Choice_list=[]
salary=input("请输入工资：")
if salary.isdigit():
    salary = int(salary)
while True:
    for index, i in enumerate(Shop_list):
        print(index, i)
    choice = input("请输入要购买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice <= len(Shop_list) and choice >= 0:
            p_item = Shop_list[choice]
            if p_item[1]<=salary:
                Choice_list.append(p_item)
                salary = salary - p_item[1]
                print("你目前还剩下 %s 钱" % salary)
                print(Choice_list)
            else:
                print("你只剩下 %s 钱啦"%salary)
        else:
            print("您所输入的%s商品列表中不存在"%choice)
    elif choice=='q':
        print("------shop------")
        for i in Choice_list:
            print(i)
        print(salary)
        #退出程序
        exit()
    else:
        print("退出")