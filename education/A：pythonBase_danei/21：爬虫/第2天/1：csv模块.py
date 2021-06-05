import csv

with open('test.csv', 'w',newline='') as f:#初始化写入文件
    writer = csv.writer(f)
    writer.writerow(["张三", 20])


with open('test.csv', 'a',newline='') as f:
    writer = csv.writer(f)
    data = [("李四",21),("王五",22)]
    writer.writerows(data)
