f=open("yesterday",'r',encoding="utf-8")
#1:这个文件是全部读取需要的行数，需要的内run比较大，所以需要一种写法，读一行然后进行覆盖
# for index,line in enumerate(f.readlines()):
#     if index == 9:
#         print("---第十行分割线----")
#         continue
#     print(line.strip())


#2:高效循环打印的方法
count=0
for line in f:
    if count==9:
        print("======我是分割线=========")
        count+=1
        continue
    print(line.strip())
    count+=1
