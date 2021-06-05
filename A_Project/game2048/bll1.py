'''
1)将核心算法粘贴进来，将所有参数，改为成员变量
'''
from A_Project.game2048.game_model import *
class GameCoreController():
    def __init__(self):
        self.__map=[
            [2, 0, 4, 2],
            [2, 2, 0, 0],
            [2, 0, 4, 4],
            [4, 0, 0, 2],
        ]
        self.__list_merge = []

    @property
    def map(self):
        return self.__map


    #练习1：定义函数，将列表中0元素，移动到末尾。 [0, 2, 0, 2]-->[2, 2, 0, 0]
    def zero_to_end(self):
        for i in range(len(self.__list_merge)-1,-1,-1):
            if self.__list_merge[i] ==0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 练习2：定义合并相同（不相邻也可以）列表元素的函数     # [2,2,0,0]    -->  [4,0,0,0]   # [2,2,2,0]    -->  [4,2,0,0]
    def merge(self):
        self.zero_to_end()# 1.将零元素移动到末尾 [2,0,2,0]    -->  [2,2,0,0]
        for i in range(len(self.__list_merge) - 1):# 2. 合并
            if self.__list_merge[i] == self.__list_merge[i + 1]:# 如果非零元素  相邻且相同
                self.__list_merge[i] += self.__list_merge[i + 1]# 将后一个元素累加到前一个元素上
                self.__list_merge[i + 1] = 0# 讲后一个元素清零
        self.zero_to_end()# 3. 将零元素移动到末尾  [2,2,2,0]    -->  [4,0,2,0]  -->[4,2,0,0]


    # 练习3:定义在控制台中绘制2048地图的函数
    def print_atlas(self,list_target):
        # 00   01   02   03
        for r in range(len(list_target)):
            for c in range(len(list_target[r])):
                print(list_target[r][c], end=" ")
        return list_target

    # 扩展作业1：定义向左移动的函数
    def move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:]=self.__map[r]
            self.merge()
            self.__map[r][:] =self.__list_merge

    def move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] =self.__list_merge

    # 练习5，定义向上移动的函数
    # 提示：将二维列表每列元素形成一维列表,交给合并merge函数,再还给二维列表
    def move_up(self):
        for c in range(4):  # 将二维列表第一列元素形成一维列表,# 00  10   20  30
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge .append(self.__map[r][c])
            self.merge()  # 交给合并merge函数
            for r in range(4):  # 再还给二维列表
                self.__map[r][c] = self.__list_merge[r]


    # 扩展作业2：定义向下移动的函数
    def move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):# 从下至上获取二维列表列元素
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):# 从左至右获取一维列表元素 # 从下至上还给二维列表
                self.__map[r][c] = self.__list_merge[3 - r]  # 0  1 2 3

def print_map(map):
    print("--------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end=" ")
        print()

if __name__ == '__main__':
    core = GameCoreController()
    print_map(core.map)
    core.move_right()
    print_map(core.map)
