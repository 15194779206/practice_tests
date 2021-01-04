import os

#1：获取当前工作目录
print(os.getcwd())

#2：改变当前脚本工作目录,然后获取目录
os.chdir("C:\Workspace-python")
print(os.getcwd())

#3：返回当前目录
print(os.curdir)
#4：获取当前目录的父目录字符串名
print(os.pardir)
#5：生成多级目录
# os.makedirs(r'C:\a\b')
#6：清理多级空文件夹
# os.removedirs(r'C:\a\b')
#7：生成单级文件夹
#8：清除单级文件夹
#9：列出所有文件夹
print(os.listdir(r'C:'))
#10：获取目录信息
print(os.stat(r'C:\work'))
#11：获取系统变量
print(os.environ)