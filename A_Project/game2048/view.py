from A_Project.game2048.bll2 import *
from A_Project.game2048.model import *

class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()


    def start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.print_map()

    def print_map(self):
        print("--------------")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c],end=" ")
            print()

    def update(self):#更新，游戏逻辑
        while True:
            self.move_map()
            if self.__controller.is_change: #判断界面是否发生变化
                self.__controller.generate_new_number()
                self.print_map()
                if self.__controller.is_game_over():
                    print("游戏结束")
                    break


    def move_map(self):
        selectc=input("wsad:")
        if selectc == 'w':
            self.__controller.move(Direction.up)
        elif selectc == 's':
            self.__controller.move(Direction.down)
        elif selectc == 'a':
            self.__controller.move(Direction.left)
        elif selectc == 'd':
            self.__controller.move(Direction.right)


    def main(self):
        self.start()
        self.update()


