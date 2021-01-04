"""
练习：使用装饰器实现：
    为两个已有功能（进入后台，删除订单），增加新功能（验证权限）
"""
def func_conditon(func):
    def warrper(*args):
        print("验证成功")
        func(*args)
    return warrper

@func_conditon
def enter_background(loginId,pwd):
    print(loginId,pwd)
    print("进入后台系统")

def delete_order(order_id):
    print("删除%d"%order_id)

enter_background('admin','123')