'''
(2)产生新数字
               ---计算所有空白位置（为0 的位置）
               ---随机选择一个位置
               ---根据概率产生数字，存入列表的相应位置
'''
from A_Project.game2048.model import *
import random
import copy
class GameCoreController():
    def __init__(self):
        self.__map=[
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4,
        ]
        # self.__map= [
        #     [2, 8, 2, 16],
        #     [8, 16, 64, 4],
        #     [4, 32, 8, 32],
        #     [8, 2, 16,0],
        # ]
        self.__list_merge = [] #用于存储去零和合并列表
        self.__list_empty_location = [] #用于存储空位置的列表
        self.is_change = False

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
    def __move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.merge()
            self.__map[r][:] = self.__list_merge

    def __move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] =self.__list_merge

    # 练习5，定义向上移动的函数
    # 提示：将二维列表每列元素形成一维列表,交给合并merge函数,再还给二维列表
    def __move_up(self):
        self.__list_merge.clear()
        for c in range(4):  # 将二维列表第一列元素形成一维列表,# 00  10   20  30
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge .append(self.__map[r][c])
            self.merge()  # 交给合并merge函数
            for r in range(4):  # 再还给二维列表
                self.__map[r][c] = self.__list_merge[r]

    # 扩展作业2：定义向下移动的函数
    def __move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):# 从下至上获取二维列表列元素
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):# 从左至右获取一维列表元素 # 从下至上还给二维列表
                self.__map[r][c] = self.__list_merge[3 - r]  # 0  1 2 3

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(4):
            for c in range(4):
                if self.__map[r][c] == 0:
                    loc = Location(r,c) #创建空位置对象
                    self.__list_empty_location.append(loc)

    def generate_new_number(self):
        ''' 随机产生新数字 '''
        self.__calculate_empty_location()
        if len(self.__list_empty_location) ==0: #无空位置
            return
        #从空位置列表中，随机选择一个元素
        loc =random.choice(self.__list_empty_location)
        #随机生成数字 eg:35%的概率random.randint(1,100)<=35
        self.__map[loc.r_index][loc.c_index] =4 if random.randint(1,10) ==1 else 2
        self.__list_empty_location.remove(loc)

    #判断是否有变化
    def move(self,dir):
        #假设没有发生变化
        self.is_change = False
        original_map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        #移动后对比地图
        self.is_change = self.__equal_map(original_map)
    def __equal_map(self,original):
        for r in range(4):
            for c in range(4):
                if original[r][c] != self.__map[r][c]:
                    return True
        return False

    def is_game_over(self):
        """游戏是否结束"""
        #1：如果存在空位置，不能结束
        if len(self.__list_empty_location) >0:
            return False
        #横纵合并
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True
            # # 如果水平方向 具有相同元素
            # for r in range(4):
            #     for c in range(3):
            #         if self.__map[r][c] == self.__map[r][c+1]:
            #             return False
            #
            # # 垂直方向
            # for c in range(4):
            #     for r in range(3):
            #         if self.__map[r][c] == self.__map[r+1][c]:
            #             return False


# if __name__ == '__main__':
#     core = GameCoreController()
#     core.print_map(core.map)
#     core.zero_to_end()
#     core.generate_new_number()
#     core.print_map(core.map)
