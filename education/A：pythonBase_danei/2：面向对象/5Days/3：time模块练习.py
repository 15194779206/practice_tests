import time
print(time.strftime("%Y %m %d %H:%M:%S",time.localtime())) #2020 06 24 16:13:00
print(time.time())  #1592986380.509147
print(time.mktime(time.localtime()))  #1592986380.0
print(time.localtime())
print(time.strptime("2020 05 12","%Y %m %d"))
#time.struct_time(tm_year=2020, tm_mon=6, tm_mday=24, tm_hour=16, tm_min=13, tm_sec=0, tm_wday=2, tm_yday=176, tm_isdst=0)
#time.struct_time(tm_year=2020, tm_mon=5, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=13


'''
1：定义函数，输入年月日，返回星期
2：定义函数：根据生日（年月日），返回活了多少天
'''
'''
# year = input("year:")
# month = input("month:")
# days = input("days:")
# numbers = ['一', '二', '三', '四', '五', '六', '七']
# one=time.strptime("%s %s %s"%(year, month, days), "%Y %m %d")
# wenkes = one.tm_wday
# print("星期%s"%(numbers[wenkes]))


year = input("year:")
month = input("month:")
days = input("days:")
borns= time.strptime("%s %s %s"%(year, month, days), "%Y %m %d")
# borns= time.strptime("2020 6 1", "%Y %m %d")
chazhi = time.time() - time.mktime(borns)
times =(chazhi)/(24*60*60)
print("存活的时间是%.1f天"%times)

'''
