#其中几个比较用的多，进行摘抄
#1：取绝对值
b=-123
print(abs(b))
#2:all()
print(all([1,-1,0]))
#3：compile()
code='''
def lib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return '----done-----'
g=lib(6)
for i in g:
    print(i)
'''
py_obj=compile(code,"err.log","exec")
exec(py_obj)

print("开始hash() 学习")
#4:hash()
a=[1,2,3,4,5,6,7,8,9]
print(hash('lalal'))
#5:zip
a=[1,2,3,4,5,6]
b=["1","2","3"]
for i in zip(a,b):
    print(i)
#结果(1, '1')(2, '2')(3, '3')按最少的拼接