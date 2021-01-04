from htmlrunner import HTMLRunner

# list = [1, 2, 3, 1]
def repect(list):
    for i in range(len(list)-1):
        #取出后面元素
        for c in range(i+1, len(list)):
            #如果发现相同
            if list[i] == list[c]:
                return True
    return False

re01 = repect([1, 2, 3, 1])
print(re01)

def re_reason(month):
    if month < 1 or month > 12:
        return "输入有误"
    if month <= 3:
        return "春天"
    if month <= 6:
        return "夏天"
    return "其他季节"

one = re_reason(5)
print(one)

#作业：4：定义函数，判断字符串中存在的中文字符数量
# 中文编码范围  0x4E00 - 0x9fA5   ord(字符)







#输出最小值
#1:首先假设第一个为最小值，然后分别获取列表中的其他值，然后在进行对比




















