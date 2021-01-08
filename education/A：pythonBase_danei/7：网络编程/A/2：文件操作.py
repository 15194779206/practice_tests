fd = open('files','r',encoding='utf-8')
'''1:read方法 '''
# data2 =fd.read()
# print(data2)
# while True:
#     data = fd.read(6)
#     if not data:
#         break
#     print("读取文件",data)


'''2:readline方法，读取一行操作'''
data = fd.readline()
print(data)

'''3:readlines方法，读取全部操作'''
data3 = fd.readlines()
for i in data3:
    print(i)

'''4：写操作'''
wf = open('writes','w+',encoding='utf-8')
wf.write("lalala\n")
wf.write("aaaaaaa\n")
fd.close()

'''writelines'''
wf.writelines(['hello\n','world\n'])


