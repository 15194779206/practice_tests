'''
前六个是红球：1--33之间的数字，且不能重复
最后一个是蓝球：1--16之间的数字
  (1)在控制台中购买彩票
  (2)随机产生一注彩票
'''
'''
ticket =[]
while len(ticket)<6:
    number = int(input("请输入第%s个红球："%(len(ticket)+1)))
    if number<1 or number >33:
        print("不在红球要求的数字里面")
    elif number in ticket:
        print("已存在")
    else:
        ticket.append(number)
# print(ticket)
while True:
    number = int(input("请输入蓝球："))
    if 1<=number <=16:
        ticket.append(number)
        break
    else:
        print("不在蓝球要求的数字里面")
print(ticket)

for i in ticket:
    print(i)
'''

#第二种方法：随机产生彩票
import random
ticket =[]
while len(ticket)<6:
    number = random.randint(1, 33)
    if number not in ticket:
        ticket.append(number)
        ticket.sort()
number = random.randint(1, 16)
ticket.append(number)
print(ticket)
















