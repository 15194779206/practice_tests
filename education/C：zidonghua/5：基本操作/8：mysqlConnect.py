import pymysql    #引用操作

#①建立连接(所需要的字段：服务器地址、服务器数据库登录用户名、密码、连接数据库名)
#如果是默认的端口可以不写
conn=pymysql.connect('localhost','root','123456','school')
#②获取游标
get_cursor=conn.cursor()
#③声明一个sql语句进行插入数据库的字符串
sql="insert into lesson values(3,'python')"
get_cursor.execute(sql)
#④提交事务
conn.commit()
#⑤关闭数据库(数据库连接需要占用资源)
conn.close()
