def make_power(y):
    def fn(x):
        return x**y
    return fn
pow2=make_power(2)
print("5的平方是：",pow2(5))  #25











