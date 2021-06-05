# 从一个文件中读取内容，修改后写入另一个文件

f=open("yesterday",'r',encoding="utf-8")
f_new=open("yesterday.bak","w",encoding="utf-8")
for line in f:
    if "具毁灭性的的那种" in line:
        line=line.replace("具毁灭性的的那种","幸福的那种")
    f_new.write(line)
f.close()
f_new.close()