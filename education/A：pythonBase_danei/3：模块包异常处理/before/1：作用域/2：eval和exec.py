x,y=100,200
print(eval("x+y",{'x':10,'y':20}))
#先找局部变量，再找全局变量



s='x=100;x+=1;print(x)'
exec(s)  #101
while True:
    s=input("请输入语句：")
    if s=="bye":
        break
    exec(s)

