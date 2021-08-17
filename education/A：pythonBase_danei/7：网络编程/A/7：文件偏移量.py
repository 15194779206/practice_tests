
fd =open('pianyi','r+')
print('当前文件偏移量',fd.tell())
fd.read(2)
print('当前文件偏移量',fd.tell())
fd.seek(0,1)#第二个参数，0代表从当前位置，1代表从开头位置，2代表末尾位置
print('当前文件偏移量',fd.tell())

