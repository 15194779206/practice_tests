'''登录注册操作'''
import pymysql

class Login(object):
    def __init__(self,database='stu',host='localhost',port=3306,user='root',passwd='123456',table='login',charset='utf8'):
        self.database = database
        self.host =host
        self.passwd = passwd
        self.port = port
        self.user =user
        self.table = table
        self.charset = charset
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database,charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def login(self,name,passwd):
        sql = "select * from %s where name='%s'and password='%s'"%(self.table,name,passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False
    def register(self,name,passwd):
        sql = "select * from %s where name='%s'and password='%s'"%(self.table,name,passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False
        sql ="insert into %s(name,password) values('%s','%s');"%(self.table,name,passwd)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            return False
        return True