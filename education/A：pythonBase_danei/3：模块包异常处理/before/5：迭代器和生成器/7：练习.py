'''
写一个程序，读入任意行的文字数据，当输入空行时结束输入打印带有行号的输入结果：
输入：hello<回车>
输入：tarena<回车>
输出如下：
第一行：hello
第二行：taerna
'''
def input_text():
    L=[]
    while True:
        s=input("请输入：")
        if not s:
            break
        L.append(s)
    return L

texts=input_text()
print(texts)
for n in enumerate(texts,  1):
    print("第%d行：%s"%n)