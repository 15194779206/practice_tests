with open('yesterday','a',encoding='utf-8') as f:
    f.write("\nwith的追加操作")

#打开多个文件
with open('yesterday','a',encoding='utf-8') as f,\
      open('write','r',encoding='utf-8') as f_second:
    print(f.write("zuijia"))
    print(f_second.readlines())