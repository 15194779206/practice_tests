#集合是无序的，天生去重

list1=[1,4,5,7,3,6,7,9]
list2=set([2,6,0,66,22,8])

#----关系测试-----
#1：去重
list1=set(list1)
print(list1)
#2：交集
print(list1.intersection(list2))
print(list1&list2)
#3：并集
print(list1.union(list2))

#4：差集 ，list1有list2中没有的
print(list1.difference(list2))
list3=set([1,4,5])
#5：子集，判断list3是否是list1的子集
print(list3.issubset(list1))
#6：父集，判断list1是否是list3的父集
print(list1.issuperset(list3))


