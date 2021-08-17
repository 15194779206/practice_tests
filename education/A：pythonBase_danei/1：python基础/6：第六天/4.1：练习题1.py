'''
1.输入一个整数 n ，代表结束的数
将1--n之间的所有的素数计算出来并存入到L列表中
  1) 最后打印此列表中的全部素数
  2) 打印这些素数的和
'''
match=int(input("请输入一个数值："))
L=[]
for i in range(1,match):
    L.append(i)

sushu=[x for x in L if x%2==1]
print("素数为：",sushu)

print('列表和是：',sum(L))
