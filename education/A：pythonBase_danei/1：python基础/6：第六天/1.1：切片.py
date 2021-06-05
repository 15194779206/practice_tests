L=[1,2,3,4,5,6]
L[::2] ='ABC'
print(L) #结果：['A', 2, 'B', 4, 'C', 6]
#对于步长不等于1的切片赋值 ，
# 赋值运算符右侧的可迭代对象提供的元素个数一定要等于切片切出的段数
'''
L[::2]='BACDEF'
print(L)  #报错
'''
Z=[1,2,3,4,5,6]
print(max(Z))

a=[1,7,3]
b=[4,5,6]
# a.append(b)  #结果[1, 2, 3, [4, 5, 6]]
a.extend(b)  #结果[1, 2, 3, 4, 5, 6]
a.sort()   #排序，正序排序
print(a)
#
# str =[]
# while True:
#     str_input = input("str:")
#     if str_input =='q':
#         break
#     str.append(str_input)
# result ="".join(str)
# print(result)

lists = ['one', 'two', 'three', 'four']
print(lists[::-1]) #['three', 'two', 'one']
print(lists[0:2]) #['one', 'two']
print(lists[:]) #['one', 'two', 'three', 'four']


list01 =[1,2]
list02 =list01
list01[0] =100
print(list02[0])