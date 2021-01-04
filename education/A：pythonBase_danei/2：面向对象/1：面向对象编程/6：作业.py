'''
1.定义一个类Human(人类)
 有三个属性：
   name,age，address
 有如下方法：
   show_info()  显示人的信息
   update_age() 方法用来让这个人的年龄增加一岁
 def input_human():
    输入下此人的信息，姓名为空结束

'''
class Human:
    def __init__(self,name ,age,address):
        self.name=name
        self.age=age
        self.address=address
    def show_info(self):
        print(self.name,self.age,self.address)
    def update_age(self):
        self.age += 1
def input_human():
    L=[]
    while True:
        name=input("姓名:")
        if not name:
            break
        age=int(input("age:"))
        address=input("地址:")
        hu=Human(name,age,address)
        L.append(hu)
    return L
def mian():  #因为input 返回的是L，返回一个列表
    docs = input_human()
    for h in docs:
        h.show_info()
    for h in docs:
        h.update_age()
    for h in docs:
        h.show_info()
mian()