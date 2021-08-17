import shutil

f1=open("文件1",encoding="utf-8")
f2=open("文件5","w",encoding="utf-8")
#将文件1中的内容拷贝到文件2中
shutil.copyfileobj(f1,f2)
shutil.copyfile("文件1","文件4")