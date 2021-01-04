#下列列表中挑出所有的偶数
list01 =[23,3,4,556,22,44,52,33]
list02= []
for item in list01:
    if item%2 ==0:
        list02.append(item)
print(list02)

#生成器函数练习
def evens():
    for item in list01:
        if item%2 ==0:
            yield item

for i in evens():
    print(i)