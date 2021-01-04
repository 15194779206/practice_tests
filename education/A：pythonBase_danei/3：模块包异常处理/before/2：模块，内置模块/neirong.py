from file_import import *
# import os
# print(file_import.__file__)
# print(os.__file__)
# print(dir(file_import))

print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fils', 'fun1', 'fun2', 'fun3', 'name1', 'name2']
#会污染别人的列表（创建的列表为'fun1', 'fun2', 'fun3', 'name1', 'name2'），等有人引用时，可以做限制
#在file_import 里面加入  __all__=['fun1','name1']，只能引用fun1和name1
