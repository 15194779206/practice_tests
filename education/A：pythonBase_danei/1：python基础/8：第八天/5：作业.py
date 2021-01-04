'''
1.输入一段字符串，打印所有输入过的字符串，但重复的只打印一次，
（不要求打印的顺序与输入的顺序一致）
输入：abcabcabc
打印: abc

2、输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数：
如：
  输入： abcdabcaba
  打印如下：
     a:4次
     b:3次
     c:2次
     。。。。不要求打印顺序
'''
'''
print("====第1题====")
chra={}
s=input("请输入一段字符串：")
chra=set(s)
print(chra)
'''

print("====第2题====")
list={}
s2=input("请输入一段字符串：")
#list=set(s2)
# for  c in list:
#     print(c,':' ,s2.count(c))
for i in s2:
    if i in list:
        list[i]+=1
    else:
        list[i]=1
print(list)  #打印出来的字典
for i in list:
    print(i,":",list[i],"次")











