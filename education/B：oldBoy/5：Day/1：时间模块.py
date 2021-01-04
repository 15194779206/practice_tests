import time

#1：获取字1970年距今的时间
x=time.time()
print("获取时间戳：",x)

#2：时间戳转换成元组的形式
y=time.localtime()
print("时间戳转换成元组的形式：",y)
#3：获取具体的时间
y=time.strftime('%Y-%m-%d-%H:%M:%S')
print(y)   #结果2018-12-06
