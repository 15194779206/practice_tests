class list_listHelper:
    @staticmethod
    def sort(target, func_condition):  # 升序
        """
        :param target: 需要排序的数据
        :param func_condition: 排序的逻辑
        func_condition类型是函数，参数是列表中两个元素，返回值是比较的结果，方式体是比较的条件
        :return:
        """
        for i in range(len(target) - 1):
            for y in range(i + 1, len(target)):
                # if target[i] >target[y]:
                if func_condition(target[i], target[y]):  # 提取共性
                    # 相当于 def func(item01,item02):return item01>item02
                    target[i], target[y] = target[y], target[i]
        return target

# 用法
# list01 = [3, 4, 1, 2]
# print(sort(list01, lambda e1, e2: e1 > e2))