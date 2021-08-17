month = int(input("请输入月份："))
day = int(input("请输入第几日："))
if month<0 or month>12:
    print("请输入正确月份")
else:
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30)
    # print(day_of_month[month-1])
    result = 0
    for i in range(month-1):
        result += day_of_month[i]

    result += day
    print(result)