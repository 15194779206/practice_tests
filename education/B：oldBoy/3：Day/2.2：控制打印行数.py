f=open('yesterday','r',encoding='utf-8')


#利用循环语句进行判断
"""
#如果到第9行，打印一行数据,这种方法比较low
data=f.readlines()
for index,line in enumerate(data):
    if index==9:
        print("---我是第九行---")
        continue
    print(line.strip())   #打印的行数
"""
#第二种方法，比较高效
count=0
for line in f:
    if count==9:
        print("======9========")
        count+=1
        continue
    print(line.strip())
    count+=1

f.close()