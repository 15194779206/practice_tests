    # 启动程序后，让用户输入工资，然后打印商品列表
    # 允许用户根据商品编号购买商品
    # 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    # 可随时退出，退出时，打印已购买商品和余额

Product_list=[
    ("苹果",200),
    ("香蕉",300),
    ("鸭梨",400),
    ("橘子",500)]

buy_list=[]
user_salary=input("请输入工资：")
if user_salary.isdigit():
    user_salary=int(user_salary)
    while True:
        for list, i in enumerate(Product_list):
            print(list, i)
        shop = input("请输入需要购买的商品编号：")
        if shop.isdigit():
            shop = int(shop)
            shop_len = len(Product_list)
            if shop < shop_len and shop >= 0:
                p_item = Product_list[shop]  # 获取这个商品
                if user_salary > p_item[1]:
                    buy_list.append(p_item)
                    print(buy_list)
                    user_salary = user_salary - p_item[1]
                    print("您目前还剩\033[31;1m%s\033[0m元钱" % user_salary)
                else:
                    print("账户还是\033[31;1m%s\033[0m ,账户余额不足"%user_salary)
            else:
                print("暂无该商品")
        elif shop == 'q':
            print("购买商品列表：",buy_list)
            exit(0)
        else:
            print("异常退出")
