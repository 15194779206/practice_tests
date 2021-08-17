#seek指的是读了多少个字符，tell是回到第几行

f=open("yesterday","r",encoding="utf-8")
print(f.readline().strip())  #读取的行数
print(f.readline().strip())
print(f.tell())  #读取的文件的字符数
print(f.seek(5))  #回到哪个字符处，回到第五个字符处
print(f.readline())