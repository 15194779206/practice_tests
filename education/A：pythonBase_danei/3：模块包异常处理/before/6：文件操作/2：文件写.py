'''
 1: 写一个程序，读入任意行的文字信息，当输入空行时结束输入，
 将读入的字符串存于列表中，然后列表里的内容写入文件input.txt中
 2：写一个程序，从input.txt中读取之前输入的数据，存于列表中，在加上行号进行打印显示
    显示格式如下：
     第一行：xxx
     第二行：www
'''
def info_down():
    L=[]
    while True:
        count=input("请输入内容：")
        if not count:
            break
        L.append(count)
    return L
def write_input(L):
    file = open('input.text', 'w', encoding='utf-8')
    for line in L:
        file.write(line)
        file.write('\n')
    file.close()
def main():
    lst=info_down()
    print(lst)
    write_input(lst)
main()

print('=======第二题========')
def read_info():
    L=[]
    files=open('input.text','r',encoding='utf-8')
    while True:
        s=files.readline()
        if not s:
            files.close()
            return L
        s=s.strip()
        index=s.find(' ')
        name=s[:index]
        for nums in enumerate(L,1):
            print(nums)
lst=info_down()
read_info(lst)