'''可迭代对象：具有__iter__()方法，可以返回迭代器的对象'''
list =["zhangsan","lisi","wangwu"]
#1.获取迭代器对象
itera = list.__iter__()
while True:
    try:
        #2：获取下一个元素（迭代过程）
        item = itera.__next__()
        print(item)
        #3：停止迭代（StopIneration 错误）
    except StopIteration as e:
        break


list2 = {"张三丰":101,"张无忌":102,"赵敏":103}
listIteror = list2.__iter__()
while True:
    try:
        item = listIteror.__next__()
        print(item,list2[item])
    except StopIteration as e:
        break
# print(list2.get("张三丰"))