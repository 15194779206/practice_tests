class AgeError (Exception):
    def __init__(self,msg,code,value):
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.value = value

class GetAge():
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 18<value<30:
            self.__age = value
        else:
            raise AgeError("我不要",27,value)
try:
    w01 =GetAge(20)
    print(w01.age)
except AgeError as e:
    print("错误信息",e.msg)
    print("错误代码行号", e.code)
    print("输入的年龄", e.value)
