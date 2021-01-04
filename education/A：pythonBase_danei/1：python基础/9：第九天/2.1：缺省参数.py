def  info(name,age=11,address="河北"):
    print("姓名：",name,"年龄：",age,"地址：",address)
info("张三",11,"美国")  #姓名： 张三 年龄： 11 地址： 美国
info("李四")  #姓名： 李四 年龄： 11 地址： 河北


def fn(a,lis=[]):
    lis.append(a)
    print(lis)
fn(1.1) #[1.1]
fn(2.2) #[1.1, 2.2]

#命名关键字传参
def myfun(a,*,k): #*后面的形参使用关键字传参
    print('a=',a,'k=',k)
#myfun(1,2)#错误
myfun(1,k=2) #k强制使用关键字传参
myfun(10,**{'k':20})  #字典关键字传参
