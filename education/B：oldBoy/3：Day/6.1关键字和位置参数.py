def test1(x,y):
    print(x,y)

test1(1,2)   #两个都是位置参数
#test1(x=1,2)    位置参数要在关键字之前，这条执行错误
test1(2,y=4)
test1(2,y=10)