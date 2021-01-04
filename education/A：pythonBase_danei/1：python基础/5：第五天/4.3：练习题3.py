'''
3：
输入一个整数（代表树干的高度）
 打印如下一棵圣诞树
 输入：3
    1
  2 2 2
3 3 3 3 3
    *
    *
    *
'''
hi = int(input("请输入树干高度："))
for i in range(1 , hi +1):
    start='2'*(2*i-1)
    lens=' '*(hi-i)
    print(lens+start)
for i in range(hi):
    Len=' '*(hi-1)+'*'
    print(Len)







