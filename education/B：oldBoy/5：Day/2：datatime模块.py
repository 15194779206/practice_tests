import datetime

#1:获取当前时间
x=datetime.datetime.now()
print("当前时间：",x)
#2：获取3个小时之后的时间
y=(datetime.datetime.now()+datetime.timedelta(hours=3))
print("3小时之后的时间：",y)
