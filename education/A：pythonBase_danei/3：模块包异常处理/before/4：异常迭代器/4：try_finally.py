def fry_egg():
    print("打开天然气！")
    try:
        try:
            count = int(input("请输入鸡蛋个数："))
            print("完成煎鸡蛋，共煎了%d个鸡蛋" % count)
        finally:
            print("关闭天然气")
    except:
        print("程序转为正常状态")

fry_egg()  #开始煎鸡蛋

print("程序正常退出!")
