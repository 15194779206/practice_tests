"""
1：画出天龙八部3D游戏技能系统设计图
    可以考虑：每个技能都做成一个类
2：面向对象知识学习
"""

class ImpactEffect:
    def impact(self):
        raise NotImplementedError()


class LowerDefense(ImpactEffect):
    def __init__(self,distance,ratio):
        self.distance = distance
        self.ratio = ratio
    def impact(self):
        print("降低%d米内，目标的防御力为%d"%(self.distance,self.ratio))


class LowerSpeed(ImpactEffect):
    """降低速度"""
    def __init__(self,time,ratio):
        self.time = time
        self.ratio = ratio
    def impact(self):
        print("降低%.2f米，时间是%d" % (self.ratio, self.time))


class Damage(ImpactEffect):
    """伤害生命"""
    def __init__(self,value):
        self.value = value
    def impact(self):
        print("伤害%d生命"%(self.value))


class SkillDeployer:
    """技能释放器"""
    def __init__(self,name):
        self.name = name
        self.__list_impact = self.__config_deployer()

    def __config_deployer(self):
        dict_skill_config={
            "韦陀杵":['LowerDefense(10,0.5)','Damage(30)'],
            "降龙十八掌": ['LowerSpeed(10,0.5)', 'Damage(30)']
        }
        list_impact_name = dict_skill_config[self.name]
        return [eval(item) for item in list_impact_name]

    def generate_skill(self):
        """生成技能"""
        print(self.name,"释放啦")
        for item in self.__list_impact:
            item.impact()


#测试
wei_tuo_chu = SkillDeployer("韦陀杵")
wei_tuo_chu.generate_skill()

























