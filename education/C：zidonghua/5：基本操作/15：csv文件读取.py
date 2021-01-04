import csv

data=csv.reader(open('D:\info.csv','r'))
for user in data:
    print(user)

data.close