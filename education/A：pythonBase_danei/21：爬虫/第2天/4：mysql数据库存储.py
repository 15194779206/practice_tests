import pymysql
db = pymysql.connect("localhost", 'root', '123456', 'maoyandb', charset='utf-8')
cursor = db.cursor()
#execute()方法第二个参数为列表传参补位
cursor.execute('insert into film values(%s,%s,%s)',['霸王别姬','张国荣','1993'])
cursor.executemany('SQL',[(),(),()])
#提交数据库
db.commit()
#关闭
cursor.close()
db.close()