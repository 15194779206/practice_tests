#重新练习代码

list01 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]
def print_map(list_target):
    for i in range(len(list_target)):
        for y in range(len(list_target)):
            print(list_target[i][y],end=" ")
        print()
# 练习1：定义函数，将列表中0元素，移动到末尾。
# [2,0,2,0]   -->  [2,2,0,0]
# [0,4,2,4]   -->  [4,2,4,0]
def zero_to_end1(list_target):
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i] ==0:
            del list_target[i]
            list_target.append(0)


# list02=[0,0,2,0]
# zero_to_end1(list02)
# print(list02)

# 练习2：定义合并相同（不相邻也可以）列表元素的函数
# [2,2,0,0]    -->  [4,0,0,0]
# [2,0,2,0]    -->  [4,0,0,0]
# [2,2,2,0]    -->  [4,2,0,0]
# [4,2,0,4]    -->  [4,2,4,0]
# [0,0,2,4]    -->  [2,4,0,0]
def merger1(list_target):
    zero_to_end1(list_target)
    for i in range(len(list_target)-1):
        if list_target[i] ==list_target[i+1]:
            list_target[i] += list_target[i+1]
            list_target[i+1]=0
    zero_to_end1(list_target)

# list03=[2,2,2,0]
# merger1(list03)
# print(list03)
'''
练习题4：定义向左移动函数
[2,0,0,2]   -->[4,0,0,0]
[2,2,0,0]   -->[4,0,0,0]
[2,0,4,4]   -->[2,8,0,0]
[4,0,0,2]   -->[4,2,0,0]
'''
list04 = [
    [2, 0, 0, 2],
    [2, 4, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]]
def move_left(list_target):
    for i in range(len(list_target)):
        merger1(list_target[i])


move_left(list04)
print("move_left",list04)
# print_map(list04)
'''
练习题5：定义向右移动函数
'''
def move_right(list_target):
    for i in range(len(list_target)):
        list_merger = list_target[i][::-1]
        merger1(list_merger)
        list_target[i][::-1] =list_merger

move_right(list04)
print("右移",list04)


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

list05 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]]
def move_up(list_target):
    for i in range(len(list_target)):
        list_merger1 = []
        # print(list_target[i][0])  #此时获取的是第一列
        for y in range(len(list_target)):
            list_merger1.append(list_target[y][i])
        merger1(list_merger1)
        # print(list_merger1)
        for y in range(len(list_target)):#返还原列表
            list_target[y][i] = list_merger1[y]

move_up(list05)
print("up",list05)

'''
练习题7：定义向下移动函数
#从上往下获取
#交给合并函数
#返还原列
'''
list06 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 4, 0, 2]]
def move_down(list_target):
    for i in range(len(list_target)):
        list_merger = []
        for y in range(len(list_target)-1,-1,-1):
            list_merger.append(list_target[y][i])
        merger1(list_merger)
        print(list_merger)
        for y in range(len(list_target)-1,-1,-1):
            list_target[y][i] = list_merger[3-y]


move_down(list06)
print("down",list06)

