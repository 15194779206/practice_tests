def fx(n):
    print("现在第",n,"层")
    if n >=3:
        return
    fx(n+1)
    print("递归的第",n,"层结束")

fx(1)
print("程序结束，")


#求100+99+98....+1的和
def mysum(x):
    if x==1:
        return 1
    return x+mysum(x-1)
print(mysum(100))