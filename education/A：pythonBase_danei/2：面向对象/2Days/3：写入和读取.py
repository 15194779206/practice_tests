class Fun:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        print("读取变量")
        return self.__name

    @name.setter
    def name(self,value):
        print("设置变量")
        self.__name = value

    # name = property(get_name,set_name)



f01= Fun(10)
f01.name = 100
print(f01.name)

