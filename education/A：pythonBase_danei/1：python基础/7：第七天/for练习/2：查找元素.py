'''
列表中是否具有相同元素
核心：所有元素间两两比较
'''

list = [1, 2, 3, 1]
state = False  #假设没有相同元素
for i in range(len(list)-1):
    #取出后面元素
    for c in range(i+1, len(list)):
        #如果发现相同
        if list[i] == list[c]:
            state =True
            break
if state:
    print("存在相同元素")
else:
    print("不存在相同元素")
