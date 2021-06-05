'''
写一个程序，让用户输入很多个正整数，当输入小于零的数时结束输入
 1：输出这些数的和
 2：输出这些数的最大的数和第二大的数
 3：删除最小的数
 4：按原来输入的顺序打印出剩余的这些数
'''
con_list=[]
while True:
    user_in = int(input("请输入数值："))
    if user_in >= 0:
        con_list.append(user_in)
    else:
        break
print('数据列表：',con_list)
con2=con_list.copy()
print('1这些数的和：',sum(con_list))
con_list.sort(reverse=True)
print('排序：',con_list)
print('2最大的数：',con_list[0],con_list[1])
l=con_list.pop(-1)
print('删除最后一个：',l)
print(con_list)
