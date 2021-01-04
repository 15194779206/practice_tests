'''
写一个函数get_score()来获取用户输入的学生成绩(0-100的整数),如果输入
出现错误，则此函数返回0，如果用户输入的数是0-100之间的数，返回这个数

'''


def get_score():
    score =input("输入学生成绩：")
    i =int (score)
    if 0 < i <= 100:
        return i
    return 0
try:
    scors=get_score()
except ValueError:
    scors =0
print('学生成绩：',scors)