#1:列表 + 运算符
list1=[1,"zhang",'11']
list2=[3.3,"lalal"]
list3=list1+list2
print(list3)

#2：* 生成重复的列表
x = [1,2]*3
print(x)  #[1, 2, 1, 2, 1, 2]
#3：*= 生成重复列表，并赋值
y=3
y *=[7,9]
print(y)

#4：练习，输入一行文字，保存在列表L中，输入空格结束输入，打印列表L内容
L=[]
while True:
    s=input("请输入一行文字：")
    if s == '':
        break
    L+=[s]
print(L[-1:-3])

