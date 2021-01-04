#截断
f=open("yesterday",'a',encoding="utf-8")
f.seek(10)
f.truncate(20)