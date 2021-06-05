import random
# 生成的验证码序列
checkcode=""
for i in range(4):
    # print(i)
    current=random.randrange(0,4)
    # print(current)
    if current !=i:
        # ascll码,生成A-Z的字母
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)
    checkcode+=str(temp)
print(checkcode)