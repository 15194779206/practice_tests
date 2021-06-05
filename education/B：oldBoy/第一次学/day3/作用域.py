name="小张"
body="women"

def Test(name):
    # 将函数中body从局部变量转换为全局变量
    global  body
    body="nan"
    print("初始的名字：",name)
    name="zhangsan"
    print("更改后的名字：",name)

Test(name)  #调用函数里面的变量
print(name) #外面声明的变量
print("body",body)



def change():
    name="lalalala"
    print(name)

change()

#局部变量修改成全局变量
names=["lalala","zhangzhang","yuoyuo"]
def changeNa():
    names[0]="changeOne"
    names[1]="张三李四"
    print(names)

changeNa()
print(names)
#输出结果['changeOne', '张三李四', 'yuoyuo']