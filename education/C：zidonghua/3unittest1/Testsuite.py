#testsuite执行一组测试用例
import  unittest
from NineTest import testMaxList    #导入类
from TenTest import loginTest

def exeSuite():
    suite=unittest.TestSuite()
    suite.addTest(testMaxList("testGetMax"))   #导入类中的方法
    suite.addTest(loginTest("testlogin"))
    print(suite)
    runner=unittest.TextTestRunner()
    runner.run(suite)

exeSuite()