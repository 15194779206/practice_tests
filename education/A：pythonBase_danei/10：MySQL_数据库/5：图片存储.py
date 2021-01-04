''' 图片存储 '''
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='stu', charset='UTF8')
#获取游标
cur = db.cursor()

with open('mysql.jpg', 'rb') as fd:
    data = fd.read()
    print(data)
#注意：读取文件千万别使用，会死机
# try:
#     sql = "insert into Images values(1,'mysql.jpg',%s)"%data
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

cur.close()
db.close()
