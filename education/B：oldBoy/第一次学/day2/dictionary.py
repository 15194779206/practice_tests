info={
    'stu001':"zhangsan",
    'stu002':"lisi",
    'stu003':"wangwu"
}
# print(info)
# 增加
# info['stu004']="zhaoliu"
# print(info)
# 删除
# del info['stu001']
# print(info)
#   第二种删除pop
# info.pop('stu002')
# print(info)
   # 随机删除
# info.popitem()
# print(info)
# 改
# info['stu003']="张三"
# print(info)
# 查
# "stu003" in info
 # 第二种
#


  # 多级元素的嵌套
av_catalog={
    "shanghia":{
        "diming":["闵行区","朝阳区"],
        "xiaochi":["烧烤","撸串"]
    },
    "beijing":{
        "diming":["北苑","清河"],
        "xiaochi":["烤鸭","鸭梨"]
    }
}
print(info.values())
print(info.keys())

# 嵌套字典的添加
av_catalog.setdefault("taiwan",{"xiaochi":["bangbang","kaoji"]})
print(av_catalog)
