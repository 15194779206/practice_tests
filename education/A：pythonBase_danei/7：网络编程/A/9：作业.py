'''
编写一个程序：
1：每隔1秒向文件practice.txt中写入一行数据，格式如下
    1.2020-9-1  12:12:10
    2.2020-9-1  12:12:11
2：该程序无限循环，ctrl+c退出
3：当重启程序时，内容会继续向下写，序号能够接上之前的
'''
import time
import signal
import sys,os



while True:
    #获取时间
    try:
        times = time.strftime("%Y-%m-%d %H:%M:%S")  # 时间获取
        rf_time = open('practice', 'r+', encoding="utf-8")
        data2 = rf_time.readlines()
        len_num = len(data2) + 1  # 编号获取
        datas = ('%s.%s') % (len_num, times)
        wf = open('practice', 'a+', encoding='utf-8')
        time.sleep(1)
        wf.write(datas + '\n')
        wf.flush()
    except KeyboardInterrupt as e:
        break
    wf.close()






