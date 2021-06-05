# buf = open('buf_test','w',0,encoding='utf-8') #0代表无缓冲，电脑不允许此操作
buf = open('buf_test','w',1,encoding='utf-8') #1代表行缓冲，加'\n'直接写入磁盘
while True:
    s=input(">>")
    buf.write(s+'\n')
    buf.flush()  #立即刷新缓冲，将内容写入磁盘
    if s =='q':
        break
buf.close()