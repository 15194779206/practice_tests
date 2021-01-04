class ImpactEffect:
    '''
        影响效果，隔离技能释放器与具体的影响效果
    '''
    def impact(self):
        pass
class LowerDefenese(ImpactEffect):
    def __init__(self,time,ratio):
        self.time = time
        self.ratio = ratio

    def impact(self):
        print("攻击距离为%.2f,时间用%d"%(self.ratio,self.time))

class LowerSpeed(ImpactEffect):
    def __init__(self, time, ratio):
        self.time = time
        self.ratio = ratio

    def impact(self):
        print("降速为%d,时间用%d" % (self.ratio, self.time))

class Damage(ImpactEffect):
    #伤害生命
    def __init__(self,value):
        self.value= value

    def impact(self):
        print("伤害值为%d"%(self.value))

class SkillDeployer:
    def __init__(self,name):
        self.name = name
        #配置释放器，存储当前技能具有的所有影响效果对象
        self.list_impact = self.__config_deployer()
    def __config_deployer(self):
        '''
        配置释放器
        :return:
        *：定义配置
        1：读取相应的影响效果
        2：创建影响效果对象
        '''
        dict_skill_config ={
            "韦陀杵":["LowerDefenese(10,0.5)","Damage(30)"],
            "降龙十八掌":["LowerSpeed(5,0.2)","Damage(80)"]
        }
        list_impact_name = dict_skill_config[self.name]
        list_impact =[]
        for item in list_impact_name:
            list_impact.append(eval(item))
        return list_impact
        #或整合成一句话
        # return [eval(item) for item in list_impact_name]

    def generate_skill(self):
        '''
        生成技能
        :return:
        '''
        for item in self.list_impact:
            item.impact()

skill = SkillDeployer("韦陀杵")
skill.generate_skill()