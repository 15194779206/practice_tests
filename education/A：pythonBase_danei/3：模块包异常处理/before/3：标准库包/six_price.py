'''
1.编写一个闹钟程序，启动时设置定时时间（小时和分钟）
到时间后打印“时间到。。。”然后退出程序
2.模拟斗地主发牌，扑克牌共54张：
 花色：
   黑桃('\u2660'),梅花('\u2663'),
   方块('\u2665'),红桃('\u2666'),
数值：
 A2-10JQK
 大小王
 三个人，每个人发17张牌，底牌留三张：
 输入回车，打印第1个人的17张牌
 输入回车，打印第2个人的17张牌
 输入回车，打印第3个人的17张牌
 再输入回车，打印出三张底牌
'''
import time

def time_stop():
    now=time.time()
    hour=int(input("请输入定时小时："))
    second=int(input("设置定时分钟："))
    seconds=second*60
    now+=seconds
    if now ==now:
        print("时间到")
        return
time_stop()

print('\u2666')










