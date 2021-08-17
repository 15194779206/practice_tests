list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["可乐", "牛奶"]
list03 = []
for i in list01:
    for y in list02:
        list03.append(i+y)
print(list03)

#列表推导式
list04 = [i+y for i in list01 for y in list02]
print(list04)
