def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))
    print("->",n)

calc(10)
#10 5 2 1  -> 1