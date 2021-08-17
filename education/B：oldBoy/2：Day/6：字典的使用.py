#字典是无序的
info ={"zhangsan":"beijing","lisi":"shanghai","wangwu":"tianjin"}
"""
#1：增加
info["zhaoliu"]="lalala"
print(info)
#2:删除
  #根据键名删除内容
info.pop("zhangsan")
print(info)
  #随机删除
info.popitem()
print(info)
#3：修改
info["zhangsan"]="zhonguo"
print(info)
#4：查找
print(info.get('lisi'))

#5：更新及替换操作，两个字典之间有相同的进行替换操作，没有相同的就在字典上面进行增加

b={2:3,"lisi":"zhongguoli"}
info.update(b)
print(info)
#{'lisi': 'zhongguoli', 'wangwu': 'tianjin', 'zhangsan': 'zhonguo', 2: 3}
"""

#6：字典的循环
for i in info:
    print(info[i])