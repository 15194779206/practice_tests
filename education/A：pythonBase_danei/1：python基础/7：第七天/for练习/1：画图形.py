for i in range(4):
    for y in range(6):
        if i%2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")  #end=' '打印一个空格
    print() #换行
print("*"*30)
for i in range(4):
    for y in range(i+1):
        # print("*", end=" ")
        print("*", end=" ")
    print()
print("*"*30)
for i in range(4):
    for y in range(i):
        print(" ", end=" ")
    for y in range(4-i):
        print("*", end=" ")
    print()
print("*"*30)