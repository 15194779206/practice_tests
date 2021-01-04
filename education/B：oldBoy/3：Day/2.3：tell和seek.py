#tell控制读取的行数，seek

f=open('yesterday','r',encoding='utf-8')
data=f.readline()
print(data)
print(f.tell())  #读取文件的字符数
print(f.seek(5)) #回到哪个字符处，回到第五个字符处s
print(f.readline())