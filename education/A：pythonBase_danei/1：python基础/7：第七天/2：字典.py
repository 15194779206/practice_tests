list ={
    1: "有1,2,3月",
    2: "有4,5,6月",
    3: "有7,8,9月",
    4: "有10,11,12月"
}
# print(list.items())
# season =int(input("请输入季度："))
# # if season<1 or season>4:
# if season not in list:
#     print("输入有误")
# else:
#     value =list[season]
#     print(value)


#2：字典的循环，获取键和值
'''
list1={
    1:'apple',
    2:"bannan"
}


for i in list1:
    print(i)
    print(list1[i])
for i,y in list1.items():  #得到的是元组
    print(i)
    print(y)
for key in list1.keys():  #获取键
    print(key)
for values in list1.values():  #获取值
    print(values)
'''

#输入字符串，输出每个字母有多少个
'''
做这道题的关键在于要分清键和值，哪个作为键，哪个作为值的问题
可以顺时思考，字母作为键，个数作为值，这样值可以增加，如果不存在可以先赋值为1

lists = {}
strs ='abcabc'
for item in strs:
    if item not in lists:
        lists[item] =1
    else:
        lists[item] +=1
print(lists)
'''

#练习题3
list_dict = {}
list_item = ["张三丰", "无忌", "赵敏"]
for item in list_item:
    print(len(item))
    list_dict[item] = len(item)
print(list_dict)


#练习题3
keys = ["张三丰", "无忌", "赵敏"]
values = [101, 102, 103]
dicts = {}
for i in range(len(keys)):
    dicts[keys[i]] = values[i]
print(dicts)

#字典的列表推导式
#{键表达式：值表达式 for 变量 in  可迭代对象}
one = {keys[i]:values[i] for i in range(len(keys))}
print(one)

#练习题4：
#键值颠倒
dict3={}
for ons,tos in dicts.items():
    dict3[tos] =ons
print(dict3)