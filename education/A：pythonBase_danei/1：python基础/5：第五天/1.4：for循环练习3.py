begin=int(input("请输入一个开始的整数："))
end=int(input("请输入一个结束的整数："))
'''
for i in range(begin , end):
    if i %2 == 0:
        continue
    print(i, end=' ')
'''
while begin < end:
    if begin % 2 == 0:
        begin += 1
        continue
    print(begin , end=' ')
    begin+=1
