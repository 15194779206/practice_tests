class Enemy:
    '''
    创建敌人类
    '''
    def __init__(self,name='',hp=0,atk=0,atk_speed=0):
        self.Name =name
        self.Hp = hp  #血量
        self.Atk = atk #攻击力
        self.Atk_speed = atk_speed # 速度

    def print_self(self):
        print(self.Name,self.Hp,self.Atk,self.Atk_speed)
'''
list_enemy=[]
for i in range(2):
    e01 = Enemy()
    e01.Name =input("name:")
    e01.Hp =input("hp:")
    e01.Atk = input("atk:")
    e01.Atk_speed = input("atk_speed:")
    list_enemy.append(e01)

for item in list_enemy:
    item.print_self()
'''

#3:定义函数，在敌人列表中根据姓名查找敌人对象
e1 = Enemy("zhang", 1, 2, 3)
e2 = Enemy("li", 4, 5, 6)
e3 = Enemy("wang", 7, 8, 9)
list_en=[e1,e2,e3]
# print(list_en)
def search_name(list_en,names):
    for item in list_en:
        # print(item.Name)
        if names == item.Name:
            return item



get_info = search_name(list_en,"li")
if get_info !=None:
    get_info.print_self()
else:
    print("没有找到")



'''
list=[]
en1 =Enemy('zhangsan',100,100,10)
while len(list)<2:

    name =input("name:")
    hp =input("hp:")
    atk = input("atk:")
    atk_speed = input("atk_speed:")
    list.append({"name:": name, "hp": hp, 'atk': atk, 'atk_speed': atk_speed})
print(en1)
'''

