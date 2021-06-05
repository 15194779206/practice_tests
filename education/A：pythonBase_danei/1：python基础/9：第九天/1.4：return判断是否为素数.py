#5定义函数，返回指定范围内的素数
def get_price(begin, end):
    list_number = []
    for number in range(begin, end+1):
        if number < 2:
            pass
        else:
            for num in range(2, number):
                if number%num == 0:
                    break
            else:
                list_number.append(number)
    return list_number


one = get_price(2, 10)
print(one)



#采用一个函数包含一个功能

def get_price(begin, end):
    list_number = []
    for number in range(begin, end+1):
        if is_im(number):
            list_number.append(number)
    return list_number

def is_im(number):
    if number < 2:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


two = get_price(2, 10)
print(two)



