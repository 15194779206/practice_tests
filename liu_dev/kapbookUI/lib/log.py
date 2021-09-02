from conf.conf import *
import json


def log_case_info(case_id, case_name, case_result, data, expect_result, actual_result):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("用例编号：{}".format(case_id))
    logging.info("用例名称：{}".format(case_name))
    logging.info("测试结果：{}".format(case_result))
    logging.info("测试数据：{}".format(data))
    logging.info("期望结果：{}".format(expect_result))
    logging.info("实际结果：{}\n".format(actual_result))
