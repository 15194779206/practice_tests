#testsuite执行一组测试用例
import  unittest
# from NineTest import testMaxList    #导入类
# from TenTest import loginTest

def testAll():
    #实现指定测试脚本文件夹进行执行所有的测试脚本
    #start_dir为找到文件目录，pattern为以什么开头或结尾的文件,此处是以什么结尾，top_level_dir顶级目录，默认参数为空
    dis=unittest.defaultTestLoader.discover(start_dir=r'D:\Workspace-python\education\4zidonghua\3unittest1'
                                            ,pattern='*Test.py'
                                            ,top_level_dir=None)   #获取一组套件执行的参数
    runner=unittest.TextTestRunner()
    runner.run(dis)

testAll()
