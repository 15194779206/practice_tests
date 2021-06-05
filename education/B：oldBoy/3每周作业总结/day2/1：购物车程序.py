Shop_list=[
    ("苹果",20),
    ("香蕉",30),
    ("草莓",50)
]
User_list=[]
Salary=input("请输入工资：")
if Salary.isdigit():
    Salary=int(Salary)
while True:
    for index, shop_list in enumerate(Shop_list):
        print(index, shop_list)
    buy_list = input("请输入要购买的商品序号：")
    if buy_list.isdigit():
        buy_list = int(buy_list)
        if buy_list < len(Shop_list) and buy_list >= 0:
            p_item=Shop_list[buy_list]  #获取列表中的内容用[]
            if p_item[1]<=Salary:
                Salary=Salary-p_item[1]
                User_list.append(p_item[0])
                print(User_list)
                print("您目前还剩下 \033[31;1m%s\033[0m 元钱"%Salary)
            else:
                print("你的钱不够啦")

        else:
            print("商品序号不存在，请重新选择")
    else:
        buy_list=='q'

        break
        exit()







