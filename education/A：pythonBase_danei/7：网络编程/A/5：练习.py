'''
从终端输入一个文件名称（可以夹带路径），将该文件复制到当前目录下，并且重名为xxx，要求可以复制所有类型文件
'''

'''
rf = open('files','rb')
writes = open('/Users/liuyang/Desktop/Workspace-python/education/A：pythonBase_danei/7：网络编程/A/testsNt', 'wb')
datas = rf.read()
writes.write(datas)
'''
try:
    rf = open('files','rb')
except Exception as e:
    print("文件未找到")
else:
    writes = open('/Users/liuyang/Desktop/Workspace-python/education/A：pythonBase_danei/7：网络编程/A/testsNt', 'wb')
    while True:
        datas = rf.read()
        if not datas:
            break
        writes.write(datas)

    rf.close()
    writes.close()

