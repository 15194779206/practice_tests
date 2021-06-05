import pymysql    #引用操作

#①建立连接(所需要的字段：服务器地址、服务器数据库登录用户名、密码、连接数据库名)
#如果是默认的端口可以不写
conn=pymysql.connect('localhost','root','123456','shuju1')
#②获取游标，获取一组结果集的集合
get_cursor=conn.cursor()
#②获取数据
get_cursor.execute("select * from logintest where username='14400000040'")
print(get_cursor.fetchone())

#④提交事务
conn.commit()
#⑤关闭数据库(数据库连接需要占用资源)
conn.close()














