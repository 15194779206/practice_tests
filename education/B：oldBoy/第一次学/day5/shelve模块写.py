import shelve
import datetime

d = shelve.open('shelve_test') #打开一个文件
name = ["alex","rain","test"]
info={"name":"zhangsa","lala":"rang"}
d["test"] = name #持久化列表
d["t1"] = info      #持久化类
d["t2"] = datetime.datetime.now()

d.close()