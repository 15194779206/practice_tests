'''
练习：将零元素移动到末尾
[2,0,2,0] -->[2,2,0,0]
[0,2,2,0] -->[2,2,0,0]
'''

#第一种思路，如果不是零，放在一个新的列表中，然后两个列表合并
#第二种思路，删除，如果是零的话，删除，然后在末尾补0,从后往前删，还是从前往后删，需要严禁处理
    #按照逻辑，可以从后往前删
print("=="*20,"0后移函数")
# def move_list(lists):
#     list_num=[]
#     for i in lists:
#         if i !=0:
#             list_num.append(i)
#     zero_list = [0]*lists.count(0)
#     news =list_num+zero_list
#     print(news)

def move_list(lists):
    for i in  range(len(lists)-1,-1,-1):
        if lists[i] == 0:
            del lists[i]
            lists.append(0)


li01 =[0,4,2,4]

move_list(li01)
print(li01)




'''
练习2：函数合并
[2,2,0,0]-->[4,0,0,0]
[2,0,2,0]-->[4,0,0,0]
'''
print("=="*20,"合并函数")
def sum_lists(target_list):
    move_list(target_list)
    for y in range(len(target_list)-1): #为什么-1，最后一个不需要和后面的比较了，没有可以比较的了
        if target_list[y] == target_list[y+1]:
            target_list[y] =target_list[y]+target_list[y+1]
            target_list[y+1] = 0

    move_list(target_list)


li = [2, 2, 2, 0]
sum_lists(li)
print(li)

print("=="*20,"获取值，表格排列")

'''
#练习3：将二维列表，以表格的格式显示在控制台中
'''
# list01 = [
#     [2, 0, 0, 2],
#     [2, 2, 0, 0],
#     [2, 0, 4, 4],
#     [4, 0, 0, 2]
# ]
list01 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]
def print_map(lists):
    for i in range(len(lists)):
        for y in range(len(lists)):
            print(list01[i][y], end=' ')
        print()

print_map(list01)


print("=="*20,"左移动")
'''
练习题4：定义向左移动函数
[2,0,0,2]   -->[4,0,0,0]
[2,2,0,0]   -->[4,0,0,0]
[2,0,4,4]   -->[2,8,0,0]
[4,0,0,2]   -->[4,2,0,0]
'''
list02 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]

def move_left(target_list):
    for i in range(len(target_list)):
        sum_lists(target_list[i])

move_left(list01)
print(list01)
print_map(list01)

print("=="*20,"右移动")
'''
练习题5：定义向右移动函数
'''
def move_right(target_list):
    for i in range(len(target_list)):
        list_merge = target_list[i][::-1]
        sum_lists(list_merge)
        target_list[i][::-1]=list_merge


move_right(list01)
print(list01)
print_map(list01)

print("=="*20,"向上移动")
'''
练习题6：定义向上移动函数
#从上往下获取
#交给合并函数
#还给原列
[2,0,0,2]   -->[2,2,2,4]-->[4,2,4,0]-->[4,2,4,0]
[2,2,0,0]   -->[0,2,0,0]-->[2,0,0,0]
[2,0,4,4]   -->[0,0,4,0]-->[4,0,0,0]
[4,0,0,2]   -->[2,0,4,2]-->[2,4,2.0]
'''
list01 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]

def move_up(target_list):
    for c in range(len(target_list)):
        list_merge=[]
        for r in range(len(target_list)):
            list_merge.append(target_list[r][c])
        sum_lists(list_merge)
        for r in range(len(target_list)):
            target_list[r][c] = list_merge[r]

    # new_list = []
    # second_list = []
    # for i in range(len(target_list)):
    #     for y in target_list:
    #         new_list.append(y[i])
    # for i in range(0, len(new_list), 4):
    #
    #     second_list.append(new_list[i:i + 4])
    # return second_list

move_up(list01)
print(list01)
print_map(list01)



print("=="*20,"向下移动")
'''
练习题7：定义向下移动函数
#从上往下获取
#交给合并函数
'''
def move_down(target_list):
    pass