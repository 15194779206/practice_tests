# 为了防止打开未关闭，用with语句
with open("yesterday","r",encoding="utf-8") as f:
    for line in f:
        print(line)

# 打开多个文件
# python3规定，每行文字最多80个字符，\为换行
# with open("yesterday","r",encoding="utf-8") as f ,\
#        open("yesterday.bak","r",encoding="utf-8") as f2:
#     for line in f:
#         print(line)
