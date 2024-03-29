import xlrd


def excel_to_list(data_file, sheet):
    data_list = []  # 新建个空列表，来盛装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_list, case_category):
    case_list = []
    for case_data in data_list:
        if case_category == case_data['case_category']:  # 如果字典数据中case_name与参数一致
            case_list.append(case_data)
    return case_list
    # 如果查询不到会返回None
