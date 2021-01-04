def goodbye(L):
    for x in L:
        print("再见:",x)
def hello(L):
    for x in L:
        print("欢迎:",x)
def fx(fn,L):
    print("f被调用")
    fn(L)

fx(hello,['Tom','jerry','spike'])
fx(goodbye,['小张','小李'])