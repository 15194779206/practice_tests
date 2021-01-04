'''pymysql基本流程演示'''
import pymysql
#链接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',database='stu',charset='utf8')
#获取游标
cur = db.cursor()
#数据操作
cur.execute("insert into myclass values(2,'zhangsan',12,'w',87)")
db.commit()
#关闭游标和数据库连接
cur.close()
db.close()