"""
用for 循环嵌套打印如下矩形
输入一个数n(10以内)代表矩形的宽度和高度
如：请输入：5
打印如下：
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
"""
#注意：打印一个空格    end=' '
num=int(input("请输入一个数："))
for i in range(1,num+1) :
    for y in range(i,i+num) :
        print(y,end=' ')
    else:
        print()