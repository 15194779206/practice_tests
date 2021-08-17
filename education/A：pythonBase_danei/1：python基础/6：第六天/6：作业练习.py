import random
#1:双色球（手动输入）
ticket=[]
while len(ticket)< 6:
    number =int(input("第%d个红球:"%(len(ticket)+1)))
    if number<1 or number >33:
        print("不在范围内")
    elif number in ticket:
        print("已存在")
    else:
        ticket.append(number)
while True:
    number =input("蓝球:")
    if 1<=number<=16:
        ticket.append(number)
        break
print(ticket)

