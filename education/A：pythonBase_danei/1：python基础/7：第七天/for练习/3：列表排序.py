'''
for循环，元素比较
'''
list01 =[1, 6, 9, 2, 3, 0]
# print(sorted(list01))
for i in range(len(list01)-1):
    # print(i)
    for c in range(i+1, len(list01)):
        if list01[i] > list01[c]:
            pad = list01[i]
            list01[i] = list01[c]
            list01[c] = pad
            #或是
            # list01[i],list01[c] = list01[c],list01[i]
print(list01)