#文件读
f=open("yesterday",'r',encoding='utf-8')
data=f.read()
print(data)
f.close()
#文件写
f_write=open("write",'w',encoding='utf-8')
f_write.write("zhangsan 添加")
f_write.close()