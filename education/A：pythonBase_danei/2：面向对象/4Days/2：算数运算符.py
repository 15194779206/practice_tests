"""运算符"""
#对象和数值做运算
class Add:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return "结果：%d"%self.x
    def __add__(self, other): #求加和
        return Add(self.x+other)
    def __pow__(self, power, modulo=None): #幂
        return Add(self.x**power)

v01 = Add(10)
v02 = v01+5#结果：15
print(v02)
v03 = v01**2 #求幂次方
print(v03) #结果：100



"""反向运算符"""
#数值和对象做运算，为反向运算符
class Add:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return "结果：%d"%self.x
    def __radd__(self, other): #求加和
        return Add(self.x+other)
    def __rsub__(self, other):
        return Add(other-self.x)
v01 = Add(10)
v02 = 5+v01#结果：15
print(v02)
v03 = 5-v01
print(v03)

"""复合运算符"""
class Add:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return "结果：%d"%self.x
    def __iadd__(self, other):
        return Add(self.x+other)
    def __lt__(self, other):
        return self.x<other
v01 = Add(10)
v01 += 5
print(v01)#结果：15

print(v01<5)  #false














