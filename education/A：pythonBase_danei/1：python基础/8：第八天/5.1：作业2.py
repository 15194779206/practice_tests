'''
1.有一只小猴子，摘了很多桃子
第一天吃了全部桃子的一半，感觉不饱又吃了一个
第二天吃了剩下桃子的一半，感觉不饱又吃了一个
。。。以此类推
到第十天，发现只剩下一个了
请问第一天摘了多少个桃子？
'''
# 10 4 1
x=1
for i in range(1,10):  #第10天是1，所以是从1-9
    x=(x+1)*2

print(x)
