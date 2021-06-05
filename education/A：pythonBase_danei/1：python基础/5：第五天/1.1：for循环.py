#1：for循环讲解
"""
s='abcdefdh'
for i in s:
    print("--->",i)
    if i =='b':
        break
else:
    print("终止")
"""
#2：打印文本里面的空格统计总数
"""
text='zhang san li si '
con=0
for i in text:
    if i ==' ':
        con+=1
print(con)
"""
#3:range函数
"""
for x in range(5,0,-2):
    print("",x)
"""
#4:根据用户输入写出步长
"""
begin=int(input("请输入开始值："))
end=int(input("请输入结束值："))
step=int(input("您希望的步长："))
for i in range(begin,end,step):
    print(i)
"""

#5:
print("第五题")
i=10
for x in range(1,i):
    print(x)
    i-=2
    print("i：",i)