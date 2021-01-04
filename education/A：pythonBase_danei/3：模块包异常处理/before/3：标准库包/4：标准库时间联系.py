'''
1:写一个程序，以电子时钟的 格式显示时间
HH：MM：SS
2：写一个程序，输入你的生日，计算出你出生的哪天是星期几？
    ②计算已出生多少天

'''
import time
def times():
    #print(time.strftime("%Y:%m:%d:%H:%M:%S"))
    ti=time.localtime()
    print(ti)
times()

#第二题
y=int(input("请输入出生的年："))
m=int(input("请输入出生的月："))
d=int(input("请输入出生的日："))
tim=time.mktime((y,m,d,0,0,0,0,0,0))
tims=time.localtime(tim)
week=tims[6]
l=[
    '星期一',
    '星期二',
    '星期三',
    '星期四',
    '星期五',
    '星期六',
    '星期日',
]
print("出生的日期为星期:",l[week])










