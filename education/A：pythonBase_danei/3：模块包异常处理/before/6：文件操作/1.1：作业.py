'''
将如下数据用文本编辑器sublime写入到data.txt文件中，
数据如下：
   小张 13800000000
   小李 13900000000
   小赵 13600000000
写程序读取数据，打印出姓名和电话号码，格式如下：
   姓名：小张  电话：13800000000
'''
'''
def File():
    files = open('data.text', encoding='utf-8')
    line = files.readlines()
    # print(line)
    L = []
    for x in line:
        L.append(x.strip().split())
    # print(L)
    for y in L:
        # print(y)
        print('姓名:', y[0], '电话:', y[1])
    files.close()
File()
'''
#第二种做法
def read_data():
    files = open('data.text', encoding='utf-8')
    L=[]
    while True:
        s=files.readline()
        if not s:
            files.close()
            print(L)
            return L
        s=s.strip()
        index=s.find(' ')
        name=s[:index]
        number=s[index+1:]
        L.append((name,number))
        print(name,number)

read_data()