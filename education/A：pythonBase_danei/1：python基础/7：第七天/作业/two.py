'''
猜拳
规则：系统随机出拳，在控制台中循环猜测
提示：
1:将胜利的策略存入容器
(
    ("石头","剪刀"),
    ("剪刀","布"),
    ("布","石头"),
)
2:将用户猜的拳与系统出拳形成一个元组
3:实现三局两胜
'''
import random
wins=(
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头"),
)
user_input_index = int(input("请输入整数(0代表石头，1代表剪刀，2代表布)："))
items =("石头", "剪刀", "布")
user_input_item = items[user_input_index]
print(user_input_item)

sys_input_index = random.randint(0, 2)
sys_input_items = items[sys_input_index]
print(sys_input_items)

if user_input_item == sys_input_items:
    print("平局")
elif (user_input_item, sys_input_items) in wins:
    print("赢了")
else:
    print("输了")







