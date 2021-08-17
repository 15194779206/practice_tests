import pymysql

db=pymysql.connect(host='localhost',user='root',passwd='123456',database='stu',charset='utf8')
#创建游标
cur = db.cursor()
while True:
    id = int(input("id:"))
    name = input('Name:')
    age = int(input("Age："))
    gender = input('m or w：')
    score = float(input("Score："))
    sql = "insert into myclass(id,name ,age,gender,score) values(%d,'%s',%d,'%s',%f)" % (id, name, age, gender, score)
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()  # 失败回滚到操作之前的状态
        print("Faild:", e)

cur.close()
db.close()
