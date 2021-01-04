'''
在控制台中循环录入字符串，输入q时退出
然后显示一个新的字符串
'''
list_res = []
while True:
    input_res = input("请输入：")
    list_res.append(input_res)
    if input_res =="q":
        break
print(list_res)
input_res ="".join(list_res[0:-1])
print(input_res)


