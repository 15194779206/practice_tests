names=['中国移动','中国电信','中国联通']
for t,n in enumerate(names,1):
    print(t,'--->',n)
# 1 ---> 中国移动
# 2 ---> 中国电信
# 3 ---> 中国联通

it =iter(enumerate(names,1))
while True:
    try:
        k,n=next(it)
        print(k,'--->',n)
    except StopIteration:
        break