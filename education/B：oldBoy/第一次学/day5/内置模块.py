# 中国是在东八区，比标准时间早八个小时
import time
import datetime
# 获取时间戳
print(time.time())   #1536885244.4153903
#
print(time.localtime())
#获取其中的时间格式如下
day=time.localtime()
print(day.tm_mon)
print(time.gmtime())

print(time.strftime("%Y:%d %H:%M:%S %Y"))
print("strpyime prctice")
print(time.strptime("2016-08:20","%Y-%m:%d"))
#把时间戳转换成字符串形式  Fri Sep 14 09:44:45 2018
print(time.ctime())
# 把元组转换成字符串形式  Fri Sep 14 09:44:45 2018
print(time.asctime())

#获取当前时间
print(datetime.datetime.now())
#获取三天后的时间
print(datetime.datetime.now()+datetime.timedelta(+3))