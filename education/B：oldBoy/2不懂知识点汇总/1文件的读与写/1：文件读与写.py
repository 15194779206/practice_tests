#1文件读取 ,r读模式
# f=open("yesterday","r",encoding="utf-8")
# data=f.read()
# print(data)


#2文件写入   ，w写模式
#是写入文件，新创建的，如果名字相同，会被清空覆盖
# f=open("yesterday","w",encoding="utf-8")
# f.write("一个新的内容,会覆盖原来的内容1")


#3:追加
f=open("yesterday","a",encoding="utf-8")
f.write("\n写入的内容被追加到后面")