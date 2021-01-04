lists = ['a', 'b', 'c']
print(enumerate(lists))
for item in lists:
    print(item)
for index, element in enumerate(lists):
    print(index, element)

#参照上述代码，自定义函数，my_enumerate
def my_enumerate():
    indexs = 0
    for item in lists:
        yield (indexs,item)
        indexs+=1

for item in my_enumerate():
    print(item)


list02=[101,102,103]
list03=["张三丰","张无忌","周芷若"]
def my_zip():
    for item in range(len(list02)):
        yield (list02[item],list03[item])

for item in my_zip():
    print(item)

lists = [item for item in list02]
print(lists)

'''列表推导式'''
list04=[1,102,103]
#使用列表推导式和生成器推导式获取list04中大于3的数据
items = (item for item in list04 if item>3)
for i in items:
    print(i)


