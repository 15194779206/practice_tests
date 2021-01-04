def mydeco(fn):
    def fx():
        print("hello word")
        fn()   #执行的是hello函数，如果带有参数，在fn和fx中加入参数
    return fx
@mydeco
def hello():
    print("hello tatena")

hello()


