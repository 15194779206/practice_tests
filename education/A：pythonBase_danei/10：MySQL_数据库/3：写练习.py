'''
数据库联系，增删改
'''
import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',database='stu',charset='UTF8')
#获取游标
cur = db.cursor()
try:
    # sql = "insert into interest values(4,'lina','draw','B','8700','good')"
    # cur.execute(sql)
    # sql = "update interest set price=6666 where name='BOb'"
    # cur.execute(sql)

    sql = "delete from myclass where score<86;"
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

#关闭游标和数据库连接
cur.close()
db.close()