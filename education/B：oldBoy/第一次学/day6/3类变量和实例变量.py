class Lei():
    #类变量
    quyu="diqiu"
    def __init__(self,name,age,school="shanghai"):
        #实例变量
        self.names=name
        self.ages=age

    def prog(self):
        print("your as %s"%self.names)
#实例化内容
jie=Lei("zhangsan",21)
jie.names="lisi"
#类变量的修改,修改后，存储在实例化对象jie中
jie.quyu="类变量"
#增加实例变量,只在实例化jie中存在
jie.close="pink_shoes"
#删除实例变量
del jie.close
print(jie.names,jie.quyu)
jie2=Lei("jieshou2",22)
#直接调用的是类变量
print(jie2.quyu)