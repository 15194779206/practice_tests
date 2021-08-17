''' 数据库联系，增删改 '''
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='stu', charset='UTF8')
#获取游标
cur = db.cursor()
try:
    sql = "select * from myclass where age=13"
    cur.execute(sql)
    # one_row = cur.fetchone() #获取第一条数据
    one_row = cur.fetchmany(2) #获取几条数据
    # one_row = cur.fetchall()
    print(one_row)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

#关闭游标和数据库连接
cur.close()
db.close()