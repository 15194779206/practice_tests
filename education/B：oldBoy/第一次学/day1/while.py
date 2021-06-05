oldage=56;
count = 0

   # 因为input默认输入类型为str，两种类型不可进行比较，所以出现错误
#

while count<3:
    age=int(input("age:"))
    if oldage==age:
        print("you are right")
        break
    elif oldage>age:
        print("down age")
    else:
        print("up age")
    count +=1
else:
    print("you have try too many")


count = 0
while True:
    print("循环",count)
    count +=1
    if count == 2:
        print("结束")
    break
