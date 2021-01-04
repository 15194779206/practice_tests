names=['zhangsan','lisi','wangwu','zhaoliu']
# 取出全
# print(names)
#取出部分值
# print(names[0],names[3])
#index从0开始，只取头不取尾   切片
# print(names[0:2])
# 从后往前数  切片
# print(names[-3:-1])
# 从-2取值
# print(names[-2:])
    # 添加
# names.append("zhangsan")
# print(names)
# 插入
# 第一个数表示在几之前插入,是下标
# names.insert(3,"charu")
# print(names)
    # 改
# names[0]="lala"
# print(names)
    # 删除
# names.remove("lala")
# 第二种删除方式,删除第一个
# names.pop(0)
# print(names)
     # 求元素是第几个
# print(names.index("lisi"))
     # 求含有几个相同的名字
# print(names.count("lisi"))
     #清空列表
# print(names.clear())
     #反转，反向输出
# print(names.reverse())
     # 合并
# name2=[1,2,3,4]
# names.extend(name2)
# print(names)
     # 删除数据
# del name2
    # 列表的循环
# for i in names:
#     print(i)

for i in names[0:-1:2]:
    print(i)
