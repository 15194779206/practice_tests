#入口程序，启动程序
import os
import sys

#路径不能写绝对，必须写相对路径
#打印文件的相对路径

#需要找到ATM的路径,dirname 返回目录名，不要文件名
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)   #添加到环境变量中
print(BASE_DIR)

from core import main

if __name__ == '__main__':  #主函数执行入口
    main.run()
