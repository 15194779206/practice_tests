'''
# 写
f=open("yesterday","w",encoding="utf-8")
f.write("我爱北京天安门")
'''

'''
# 追加
f=open("yesterday","a",encoding="utf-8")
f.write("我爱北京天安门...\n")
f.write("天安门太阳升...\n")
'''

#根据行数进行读取
f=open("yesterday","r",encoding="utf-8")   #文件句柄
'''
for line  in f:
    print(line.strip())
'''

'''
# 设置读取行数
count=0
for line in f:
    if count==3:
        print("-------截断-----")
        count+=1
        continue
    print(line.strip())
    count+=1
'''

#tell打印当前的位置
print(f.tell())
print(f.readline())   #打印当前行数
#seek回到哪个地方
f.seek(0)
print(f.read(5))    #打印多少个字符



