'''
有若干个图形（圆型，矩形。。。）
每种图形，都可以计算面积
定义图形管理器，记录所有图形，提供计算总面积的方法
要求：增加新的图形，不改变图形管理器代码
'''
'''
想法：首先不确定有几个图形，每个子类计算面积，父类
'''
class GraphicManager:
    def __init__(self):
        self.__graphics =[]

    def add_graphic(self,g):
        self.__graphics.append(g)

    def get_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area +=item.get_area()
        return total_area

class Graphic:
    '''代表所有的图形'''
    def get_area(self):
        pass

class Circle(Graphic):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return self.radius*self.radius*3.14


class Rectangle(Graphic):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width*self.height



manager = GraphicManager()
manager.add_graphic(Rectangle(4,6))
manager.add_graphic(Circle(5))
print(manager.get_total_area())




















