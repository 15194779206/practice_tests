try:
    f=open('data.text','rb')
    print("打开文件成功")
    b=f.read()
    print('字节串：',b)
    s=b.decode('utf-8')
    print('转码后',s)
except IOError:
    print('文件打开失败')