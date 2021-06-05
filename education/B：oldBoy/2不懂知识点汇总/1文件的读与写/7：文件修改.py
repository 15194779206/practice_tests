#文件修改就是一个文件读，一个文件写
f=open("yesterday",'r',encoding="utf-8")  #此文件进行读
f_new=open("yesterday2",'w',encoding="utf-8")  #此文件进行写
for line in f:   #循环f中的语句，修改里面的内容，然后添加到新的文件中
    if "昨日当我年少轻狂" in line:
       line=line.replace("昨日当我年少轻狂","我就是很轻狂")
    f_new.write(line)

f.close()
f_new.close()
