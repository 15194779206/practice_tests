f=open("yesterday",'r+',encoding="utf-8")
print(f.readline().strip())
f.write("-----新写入的内容------")
print(f.readline())

#"rb"读模式----表示处理二进制文件
f=open("yesterday",'rb')

#"wb"写模式---表示处理二进制文件
f=open("yesterday",'wb')  #encode()--str转化成byte类型
f.write("写入二进制的内容---")