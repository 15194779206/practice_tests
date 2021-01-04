import pymysql    #引用操作

#①建立连接(所需要的字段：服务器地址、服务器数据库登录用户名、密码、连接数据库名)
#如果是默认的端口可以不写
conn=pymysql.connect('localhost','root','123456','shuju1')
#②获取游标，获取一组结果集的集合
get_cursor=conn.cursor()
#③声明一个sql语句进行插入数据库的字符串
sql="insert into logintest(id,username,password) values(%s,%s,%s)"%(4,'14400000052',1234)
try:
    get_cursor.execute(sql)
    # ④提交事务
    conn.commit()
except:
    print("出现错误了")
    conn.rollback()  #发生错误时回滚
#⑤关闭数据库(数据库连接需要占用资源)
conn.close()