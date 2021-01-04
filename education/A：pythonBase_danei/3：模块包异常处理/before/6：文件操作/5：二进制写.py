try:
    f = open('betys', 'wb')
    f.write(b"hello\xe4\xb8\xad\xe5\x9b\xbd") #hello后面是中国的二进制
    s='我是汉字'
    r=f.write(s.encode('utf-8'))
    print("写入文字：",s,"，共写入",r,"字节")  #写入文字： 我是汉字 共写入 12 字节
except IOError:
    print("文件打开失败")