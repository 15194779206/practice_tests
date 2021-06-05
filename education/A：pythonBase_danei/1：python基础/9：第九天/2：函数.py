#1：位置传参
def fx(a,b,c):
    print('a=',a,'b=',b,'c=',c)
fx(1,2,3) #a= 1 b= 2 c= 3

#序列传参
def fx(a,b,c):
    print('a=',a,'b=',b,'c=',c)
s1=[11,22,23]
fx(*s1)  #相当于 fx(s1[0],s1[1],s1[2])

#关键字传参
def fx(a,b,c):
    print('a=',a,'b=',b,'c=',c)
fx(c=1,b=2,a=3)

#字典关键字传参
def fx(a,b,c):
    print('a=',a,'b=',b,'c=',c)

d={'a':'name','b':'age','c':'hobby'}
fx(**d)

#函数练习
def rectangle_shape(row,slu):
    for i in range(row):
        for y in range(slu):
            print("#", end=" ")  #end=' '打印一个空格
        print() #换行

rectangle_shape(3,4)

def shape_angle(row):
    """

    :param row: 代表行
    :return:
    """

    for i in range(row):
        for c in range(i+1):
            print("#", end=" ")
        print()

shape_angle(4)