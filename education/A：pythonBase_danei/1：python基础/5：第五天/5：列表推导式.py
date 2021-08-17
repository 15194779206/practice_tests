list01 = [1, 2, 3, 4]
list02 =[x**2 for x in list01 if x%2==0]

print(list02)

'''
练习：使用range生成1--10之间的数据，存入列表list01中，
'''
list1=[]
for i in range(1,11,1):
    list1.append(i)

print(list1)
list2=[x for x in list1 if x%2==0]
print(list2)

list3=[x for x in list1 if x%2==1]
print(list3)
