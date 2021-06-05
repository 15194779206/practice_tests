L=[2,3,5,7]
it=iter(L)
print(next(it)) #2
print(next(it)) #3
print(next(it)) #5
print(next(it)) #7
try:
    print(next(it)) #报错 StopIteration
except StopIteration as e:
    print("执行到最后一个了",e)
print(it)

'''
练习：已知有一个集合：
s={"工商银行","建设银行","中国银行","农业银行","上海银行"}
1.用for语句遍历集合中的元素并打印
2.将上面的for语句改写成while语句实现上面相同的功能
'''
s={"工商银行","建设银行","中国银行","农业银行","上海银行"}
# for x in s:
#     print(x)
it =iter(s)
print(next(it))
print(next(it))
print(next(it))

while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break


















