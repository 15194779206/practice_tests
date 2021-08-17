"""
    对列表常用操作的模块（完整版）
"""
class ListHelper:
    """
        列表助手类:定义对列表的通用操作
        list_target为列表
        func_condition 为判断函数
    """
    @staticmethod
    def find_all(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(list_target,func_condition):
        for item in list_target:
            # if item.age < 30:
            if func_condition(item):
                return item

    @staticmethod
    def count(list_target,func_condition): #求有多少个
        int_count = 0
        for item in list_target:
            if func_condition(item):
                int_count += 1
        return int_count

    @staticmethod
    def sum(list_target, func_condition): #求需获取值的总数
        value_sum = 0
        for item in list_target:
            value_sum += func_condition(item)
        return value_sum

    @staticmethod
    def get_max(list_target, func_condition): #对比，求某一最大值
        value_max = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(value_max)<func_condition(list_target[i]):
                value_max = list_target[i]
        return value_max

    @staticmethod
    def get_min(list_target,func_condition):
        """
            通用的查找最小值方法
        :param list_target: 对象列表
        :param func_condition: 查找条件 func(对象): reutrn 对象.属性
        :return: 最小值
        """
        value_min = list_target[0]
        for i in range(1, len(list_target)):
            # if value_min.atk>list_target[i].atk: #相当于如下代码，变化点为atk
            if func_condition(value_min) > func_condition(list_target[i]):
                value_min = list_target[i]
        return value_min

    @staticmethod
    def exists(list_stu,func_condition):  #判断是否包含满足条件的对象
        for item in list_stu:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def order_by(list_target,func_condition):
        """
            对象列表，进行升序排列。
        :param list_target: 对象列表
        :param func_condition: 排序条件
        """
        for r in range(len(list_target) - 1):
            for c in range(r+1,len(list_target)):
                if func_condition(list_target[r]) > func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]
        return list_target

    @staticmethod
    def order_by_descending(list_target,func_condition):  #降序排序
        for r in range(len(list_target) - 1):
            for c in range(r+1,len(list_target)):
                if func_condition(list_target[r]) < func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]
        return list_target

    @staticmethod
    def delete_all(list_target, func_condition):
        count = 0
        # 倒序删除列表中元素
        for i in range(len(list_target)-1,-1,-1):
            if func_condition(list_target[i]):
                del list_target[i]
                count += 1 # 统计删除的个数
        return count

    @staticmethod
    def select(list_target,func_condition):  #获取满足条件的值
        for item in list_target:
            if func_condition(item):
                yield item

    

#用法
#list_skill为列表
# for item in ListHelper.find_all(list_skills,lambda e:e.id>101):
#     print(item.id)


