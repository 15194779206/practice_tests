name='zhangsan'
age=28
print ("name:%s , age %d " %(name,age))

a=2
b=3
if a>b:
    print("max:%d"%b)
else:
    print("max:%d"%a)

#  包含
str="lala"
str2="lalalin"
# 不相等  not in
"""
if str in str2:
    print("包含")
else:
    print("不包含")
"""

# for in 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

for ma in range(5):
     print(ma)


# 键值对，数组可以包含字符串，字符和数字
value=["1",2,"3","张三"]
z={"name":"张三","age":"12","address":"beijing"}
#得到的是K值
for k in z:
    print(k)
for k,v in z.items():
    print (k,v)