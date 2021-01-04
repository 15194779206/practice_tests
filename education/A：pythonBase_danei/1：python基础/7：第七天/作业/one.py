'''
在控制台中录入5个学生信息（姓名/年龄/性别）
[
]
# {
    #     "names": "zhangsan",
    #     "ages": 13,
    #     "sexs": "男"
    # },
    # {
    #     "name": "lisi",
    #     "age": 14,
    #     "sex": "女"
    # }
'''
list_stu_info =[]
for i in range(2):
    dict_stu={}
    dict_stu["name"] = input("请输入姓名：")
    dict_stu["age"] = input("请输入年龄：")
    dict_stu["sex"] = input("请输入性别:")
    list_stu_info.append(dict_stu)

for i in list_stu_info:
    for key,values in i.items():
        print(key,":",values)