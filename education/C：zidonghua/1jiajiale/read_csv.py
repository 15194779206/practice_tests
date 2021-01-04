import csv
my_file='data.csv'
data=csv.reader(open(my_file,'r+'))

for user in data:
    print(user)