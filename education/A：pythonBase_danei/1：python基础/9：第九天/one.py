import unittest
import time
#导入该类之前需要先配置环境
import htmlrunner
# from htmlrunner import HTMLRunner
def  testAll():
    #实现指定测试脚本文件夹进行执行所有的测试脚本
    dis = unittest.defaultTestLoader.discover(start_dir=r'/Users/liuyang/Desktop/Workspace-python/education', pattern='*Test.py',top_level_dir=None)
    print(dis)
    #/Users/liuyang/Desktop/Workspace-python/education
    #获取系统时间
    timepath=time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    # 文件存放的目录，creTest.html是每次执行生成的
    path = open('C:\Workspace-python\jiajiabank\HTMLTest\crmTest%s.html' % timepath, 'wb')
    #第一个参数stream表示的是报告生成的路径
    #title表示的是报告的标题
    #description表示的是报告的描述
    # runner=HTMLRunner.HTMLTestRunner(stream=path,title='所有测试脚本文件报告',description='以下是报告详情')
    runner =htmlrunner.HTMLRunner(stream=path,title='所有测试脚本文件报告',description='以下是报告详情',output='')
    runner.run(dis)

testAll()