rf = open('files','rb')
data=rf.read()
print(data)

#二进制打开文件

rd = open('11.png','rb')
data2=rd.read()
print(data2)

wb = open('files','wb+')
data3 = wb.write(b"hello world")
print(data3)