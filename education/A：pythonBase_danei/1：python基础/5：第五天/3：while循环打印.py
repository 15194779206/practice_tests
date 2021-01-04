win=int(input("请输入三角形的宽度："))
hi=1
while hi <= win:
    print("*"*hi)
    hi += 1

print("第二种图形")
se=1
while se <= win:
    print(" "*(win-se)+"*"*se)
    se += 1

print("第三种图形")
th=1
while th <= win :
    print(" "*th+"*"*(win-th+1))
    th+=1

print("第四种图形")
fo=0
while fo < win:
    print("*"*(win-fo))
    fo+=1

print("第五种图形")


