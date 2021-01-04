'''
#1:
1.有字符串列表如下：
 L=[’tarena ' , 'xiaozhang ' , 'hello ' ]
用推导式生成如下字典：
 d={’tarena ' :6, 'xiaozhang ':9 , 'hello ':5 }
 #2:
 有两个列表：
 no=[1001, 1002, 1003 , 1004]
 names=['Tom ' ,'Jerry' , 'Spike' ,' Tyke']
 用no 中的编码作为键，以names中的字符串作为值，生成相应的字典
'''

print("第一题：")
L=['name','zhangsan','age']
for i in L:
    lens=len(i)

first={i : lens for i in L  }
print(first)

print("第二题：")
no = [1001, 1002, 1003, 1004]
names = ['Tom ', 'Jerry', 'Spike', ' Tyke']
second={no[i]: names[i] for i in range(len(no)) }
print(second)














