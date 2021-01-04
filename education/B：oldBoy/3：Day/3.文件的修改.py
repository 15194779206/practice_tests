"""
1:如果进行修改文件，就会破坏源文件，
所以需要打开一个文件读取，然后写入另一个文件中
"""
f=open('read','r',encoding='utf-8')
f_new=open('writefile','w',encoding='utf-8')
for i in f:
    print(i.strip())
    if "我经历的爱情总是最具毁灭性的的那种" in i :
        i=i.replace("我经历的爱情总是最具毁灭性的的那种","我总是那么快乐")
    f_new.write(i)  #if和else中都有f_new.write(i)，两个合成一个写成这样


