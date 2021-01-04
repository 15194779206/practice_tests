s1={1,2,3}
s2={2,3,4}

#交集 &
print(s1&s2)

#并集  |
print(s1|s2)

#补集   -
print(s1-s2)#生成属于s1但是不属于s2的值
print(s2-s1)

#对称补集
print(s1^s2)

#子集  <
l={1,2,3}<{1,4}
print(l)  #false

#超集   >
l={1,2,3}> {1,3}
print(l)  #true

