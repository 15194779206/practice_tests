def get_score():
    while True:
        try:
            score = int(input("score:"))
        except Exception as e:
            print("输入有误")
            continue
        if 1<=score <=100:
            return score
        print("不在指定范围内")

        

get_score()