'''
 {  键表达式：值表达式   for  变量  in  可迭代对象 [ if  真值表达式  ] }
 注：  [ ] 的内容代表可省略

 作业：生成一个字典，键wei10以内的数字，值为键的平方
'''

d={ x : x**2 for x in range(3) }
print(d)  #{0: 0, 1: 1, 2: 4}