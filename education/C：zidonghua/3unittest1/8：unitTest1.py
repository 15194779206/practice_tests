class Maxtext:
    def  getMax(self,list):
        max=0
        for i in list:
            if max<i:
                max=i
        return max


max1=Maxtext()
list=[1,2,3,4]
try:
    assert max1.getMax(list)==3  #max1实例化对象，getMax是方法
except:
    print('预期与实际不符')
