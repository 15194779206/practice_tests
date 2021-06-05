import xlrd
def get_data(sheet,module):
    data_file = r"D:\Workspaces-python\Test_interface\data\data.xlsx"
    # data_file='/Users/liuyang/Desktop/Workspace-python/Test_interface/data/data.xlsx'
    data = xlrd.open_workbook(data_file)
    table = data.sheet_by_name(sheet)
    sheet_name = table.row_values(0)  #获取sheet文件中表头
    for i in range(1,table.nrows):   #table.nrows有效行数，根据行数获取值
        lists = dict(zip(sheet_name,table.row_values(i)))
        if lists['module'] ==module:
            yield lists
        else:
            continue

# lists = get_data('Login')
# for i in lists:
#     print(i)
# # print(lists)

# list01 = [(item['id'],item) for item in lists]
# print(list01)

'''
def readtdata(sheet, module):
    try:
        wb = xlrd.open_workbook(data_file)                  # 打开excel
    except Exception as e:
        print('数据文件不存在！')
    else:
        try:
            sh = wb.sheet_by_name(sheet)                    # 获取工作簿
        except Exception as e:
            print('excel中指定sheet不存在！')
        else:
            header = sh.row_values(0)                           # 获取标题行数据
            for i in range(1, sh.nrows):                        # 跳过标题行，从第二行开始取数据
                data = dict(zip(header, sh.row_values(i)))      # 将标题和每行数据组装成字典
                # print(data)
                if data['module'] == module:                    # 如果所取用例数据是指定模块，则通过生成器返回给调用者
                    yield data
                else:
                    continue

'''
