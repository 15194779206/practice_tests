try:
    file = open('files',encoding='utf-8')
    s=file.readline()
    print("one:",s)
    file.close()
    print("文件已关闭")
except IOError :
    print("文件打开失败")
#打开失败会报错误IOError