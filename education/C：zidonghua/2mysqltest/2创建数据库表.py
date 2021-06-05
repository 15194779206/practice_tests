import pymysql

conn=pymysql.connect('localhost','root','123456','shuju1',charset='utf8')
cursor=conn.cursor()
# cursor.execute('drop table if exists employee1')
sql = """create table advertising (
         name  char(50) not null,
         ad_link  char(50),
         """
cursor.execute(sql)
conn.close()