class Role:
    n=123   #实例变量
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def got_shot(self):
        print("%s is beautiful"%self.Name)
    def __del__(self):
        print("%s is 析构函数"%self.Name)

r1=Role("zhangsan",22)
r1.sex="女"   #增加
r1.Name="大雷"  #修改
del r1.Age  #删除
r1.n='改类变量'

print(r1.sex , r1.Name , r1.n)  #结果：女 大雷 改类变量
#实例化中修改类变量，相当于在自己的内容中创建一个 r1.n='改类变量'

r2=Role("lisi",30)
print(r2.n)   #结果：123




