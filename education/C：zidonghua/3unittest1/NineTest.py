
#需要引入unittest框架
#如果需要声明一个测试类的话，并且引用unittest框架的话
#则需要使用该测试类进行继承于testcase类
import  unittest

class MaxList:
    def  getMax(slef,list1):
        max=0
        for i in list1:
            if max<i:
                max=i
        return max


class testMaxList(unittest.TestCase):
    #进行测试maxlist类中的getMaxt方法
    #声明一个测试方法
    def testGetMax(self):
        maxClass=MaxList()
        #声明一个列表-----预期最大值123
        list1=[1,3,4,123]
        #获取的是实际最大值
        max=maxClass.getMax(list1)
        #assertEqual是unittest的testcase类的一个断言方法
        #msg同样是针对存在异常时才会将该信息输出，该参数可以省略
        self.assertEqual(123,max,'预期与实际不一致')
#main方法是unittest中的主方法
#不同的框架具有不同的运行器：
#如果不引用unittest框架的则执行的是python运行器；
#如果引用则执行的是unittest运行器；同样还有报告运行器，套件运行器等
if __name__=='__main__':
    unittest.main()

