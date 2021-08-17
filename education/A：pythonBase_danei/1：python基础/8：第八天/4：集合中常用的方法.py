L={'name','age'}
L.add("hobby")
print(L)

#集合推导式：天生去重复
# { 表达式   for  变量  in  可迭代对象  [ if  真值表达式 ] }
L={1,2,1,2,3,4,5}
Z={x for x in L}
print(Z)  #{1, 2, 3, 4, 5}
























