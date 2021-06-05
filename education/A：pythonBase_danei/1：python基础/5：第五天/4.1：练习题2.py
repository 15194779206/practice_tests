'''
2：
输入一个整数（代表树干的高度）
 打印如下一棵圣诞树
 输入：2
  *
* * *
  *
  *
  输入：3
    *
  * * *
* * * * *
    *
    *
    *
'''

hi =int(input("输入高度："))
for i in range(1 , hi+1):
    start='*'*(2*i-1)
    blans=' '*(hi-i)
    print(blans+start)
for i in range(hi):
    print(' '*(hi-1)+'*')