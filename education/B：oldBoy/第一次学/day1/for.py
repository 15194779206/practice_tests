'''
for i in range(10):
    print("poop:",i)

# range()可放入多个参数
for i in range(0,10,3):
    print(i)
'''

# 输入三次出现提示信息
oldage=56;
count = 0
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
    if count==3:
        continue_num=print("dou you need more try?")
        if count !="n":
            count=0
#else:
  #  print("you have try too many")
