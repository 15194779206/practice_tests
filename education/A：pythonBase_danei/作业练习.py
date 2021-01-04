'''
1：存钱，直接存入
2：取钱，需要交手续费，金额的5%
'''
data ={
    'all_money': 1500
}

#存钱
def save_money():
    save_num = int(input("请输入存入的金额："))
    data['all_money'] = save_num
    return data['all_money']

#花钱
def spend_money():
    spend_num = int(input("请输入花销金额："))
    data['all_money'] -= spend_num*(1+0.05)
    print(data['all_money'])


choose_list='''
    1:"存钱",
    2:"花钱",
'''
print(choose_list)
choose = input("请输入操作：")
if choose == "1":
    save_money()
elif choose == "2":
    spend_money()

















