import shelve
import datetime

d = shelve.open('shelve_test') #打开一个文件
print(d.get("test"))
print(d.get("t1"))