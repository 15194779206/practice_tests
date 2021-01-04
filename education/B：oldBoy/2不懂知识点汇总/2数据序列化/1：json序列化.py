import json

data={
    '北京':{"name":"alex"},
    '上海':{"names":"zhangsan"}
}
f=open("test.text",'w')  #打开文件进行写入
f.write(json.dumps(data))





# if __name__=='__main__':
#     test()