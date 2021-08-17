#取绝对值
# print(abs(-1))

# filter
res=filter(lambda n:n>5,range(10))
for i in res:
    print(i)   #结果6,7,8,9

res2=map(lambda n:n,range(10))
for i in res2:
    print(i)  #结果0,1,2,3,4,5,6,7,8,9


list={1:2,3:-2,11:22,111:222,4:-11}  #字典的特性是无序的
print(list)  #字典是无序的
print(sorted(list))  #根据键进行排序
print(sorted(list.items()))   #转化成列表进行排序