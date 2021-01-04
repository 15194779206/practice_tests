'''
在控制台中随意录入多个字符串，
按q退出，显示所有不重复的字符串
'''
str_list =set()

# while True:
#     str_input = input("请输入字符串：")
#     if str_input == 'q':
#         break
#     str_list.add(str_input)
# print(str_list)

'''
练习题2：
经理：[曹操，刘备，孙权]
技术员：[曹操，刘备，张飞，关羽]
'''
manage_list ={"曹操", "刘备", "孙权"}
eneloge_list ={"曹操", "刘备", "张飞", "关羽"}

#交集
pra_one = manage_list & eneloge_list
print(pra_one)
#补集
pra_two = manage_list - eneloge_list
print(pra_two)

pra_three = eneloge_list - manage_list
print(pra_three)

#判断
if  "张飞" in manage_list:
    print("是经理")
else:
    print("不是经理")

#对称补集
pra_four= manage_list ^ eneloge_list
print(pra_four)

#并集求和
pra_five= manage_list | eneloge_list
print(len(pra_five))