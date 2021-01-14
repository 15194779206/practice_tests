import requests
from bs4 import BeautifulSoup
import re
import random
import json

Login_url ='https://test.kapbook.cn/login/check_login_ajax'
Save_company = 'https://test.kapbook.cn/user/save_company_info_ajax'
Save_company1 ='https://test.kapbook.cn/user/index?from=login'
createplan_url='https://test.kapbook.cn/equity_plan/online/add_ajax'
header= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
Login_data={
    'email': '15028217377',
    'password': 'MTIzNDU2',
    'type': '1'
}
response = requests.post(url=Login_url,data=Login_data,headers=header)
print(response.json())



'''

times = response.cookies['request_time']
tokens = response.cookies['token']
# print(tokens)

cookie = {
    "request_time":times,#'1607408394'
    "token":tokens, #'4568b716fdec4d34ebe3b36d02d465a2'
}
company_list =requests.get(url=Save_company1,cookies=cookie)
# print(company_list.text)
soup = BeautifulSoup(company_list.text,'html.parser')
dataToken_list = soup.find_all(class_='userVerify')
tokens_list = [item.get('data-token') for item in dataToken_list]  #获取company列表
# print(random.choice(tokens_list)) #获取随机token,进入公司
creatCookie={
    "request_time":times,
    "token":tokens,
    "company_token":tokens_list[0]
}
print('随机进入公司',random.choice(tokens_list))

#创建计划需要提前获取一些信息
addPlan_pre = "https://test.kapbook.cn/equity_plan/online/add"
addPlan_request = requests.get(url=addPlan_pre,cookies= creatCookie)
# print(addPlan_request.text)
soup_creatPlan = BeautifulSoup(addPlan_request.text,"html5lib")
pattern = re.compile(r"var initInfo = (.*?);$")
script = soup_creatPlan.find("script", text=pattern)
print(script) #<class 'bs4.element.Tag'>
'''

#注册
'''
regiser_url ="https://test.kapbook.cn/register/check_mobile"
register_data={
    "mobile": "15194779201",
    "nationcode_id": "214",
    "nationcode": "86"
}
register_req = requests.post(url=regiser_url,data=register_data)
print(register_req.json())
'''
'''


#修改对公账户
# '''
# modifyBank_url = 'https://test.kapbook.cn/company/setting/operate_corporate_account'
# modifyBank_data={
#     "name": "0910测试有限公司",
#     "bank_branch_name": "建设银行",
#     "number": "6217000000000000123"
# }
# modifyBank_req = requests.post(url=modifyBank_url, cookies=creatCookie, data=modifyBank_data)
# print(modifyBank_req.json())
# '''
#



'''
createPlan_step6Data={
    "step": "6",
    "company_name": "20201209测试有限公司",
    "financing_stage_id": "2",
    "manage_company_user_id": "33891,15028217377,--",
    "valuation_price":"",
    "registered_capital": "1000000.00",
    "unit": "1000000",
    "size_registered_capital": "10000",
    "per": "1",
    "size": "10000",
    "source_type": "2",
    "window_type":" 1",
    "interval_time":"",
    "exercise_retention_amount": "1",
    "exercise_retention_type": "1",
    "exercise_admin_cuid": "33891",
    "exercise_admin_cuid_name": "15028217377",
    "is_upload_voucher": "2",
    "buyback": "[]",
    "dataMsg": "[object Object]",
    "exerciseMsg": "[object Object],[object Object]",
    "additional_clause": "",
}

createPlan_step6_req = requests.post(url=createplan_url,cookies =creatCookie,data=createPlan_step6Data)
# print(createPlan_step6_req.json())


createPlan_endData={
    "step": "7",
    "company_name": "20201209测试有限公司",
    "financing_stage_id": "2",
    "manage_company_user_id": "33891,15028217377,--",
    "valuation_price":"",
    "registered_capital": "1000000.00",
    "unit": "1000000",
    "size_registered_capital": "10000",
    "per": "1",
    "size": "10000",
    "source_type": "2",
    "window_type":" 1",
    "interval_time":"",
    "exercise_retention_amount": "1",
    "exercise_retention_type": "1",
    "exercise_admin_cuid": "33891",
    "exercise_admin_cuid_name": "15028217377",
    "is_upload_voucher": "2",
    "buyback": "[]",
    "dataMsg": "{'1':[{'sign_property_id':'301','company_user_id':0,'sort':1},{'sign_property_id':'103','company_user_id':'33891','company_user_name':'15028217377','nick_name':'公司盖章','sort':2}],'2':[{'sign_property_id':'301','company_user_id':0,'sort':1},{'sign_property_id':'601','company_user_id':0,'sort':2},{'sign_property_id':'103','company_user_id':'33891','company_user_name':'15028217377','nick_name':'公司盖章','sort':3}]}",
    "exerciseMsg":"[{'sign_property_id':'401','sort':1},{'sign_property_id':'501','sort':2}]",
    "document_path_1": createPlan_step6_req.json()['error_msg']['1'],
    "document_path_11": createPlan_step6_req.json()['error_msg']['11'],
    "document_path_2": createPlan_step6_req.json()['error_msg']['2'],
    "document_path_12": createPlan_step6_req.json()['error_msg']['12'],
    "document_path_3": createPlan_step6_req.json()['error_msg']['3'],
    "document_path_6": createPlan_step6_req.json()['error_msg']['6'],
    "plan_name": "股权激励计划test3",
    "notes":"",
    "plan_is_open_overfulfill": "0"
}

createPlan_endReq =requests.post(url=createplan_url,cookies =creatCookie,data= createPlan_endData)
print(createPlan_endReq.status_code)
'''

#添加参与方信息
'''
addEmployee_url ="https://test.kapbook.cn/company/people/add_manager_ajax"
employee_data={
    "type": "1",
    "board_type": "0",
    "access_role_id": "3",
    "access_role_val": '{}',
    "add_type": "1",
    "is_send_email": "0",
    "nationcode_id": "214",
    "nationcode": "86",
    "name": "测试2",
    "email": "1234567@qq.com",
    "phone": "15194770023",
    "certificate_type": "2",
    "certificate_code": "1234512",
    "dimission":"0",
    "id_no":'',
    "department":'',
    "position":'',
}  #{'error_code': True, 'error_msg': 33935}
add_response = requests.post(url=addEmployee_url,cookies=creatCookie,data=employee_data)
print(add_response.json())
addPeo_detial ="https://test.kapbook.cn/company/people/get_userinfo_by_id"
addPeoDetial_data ={
    "id":add_response.json()['error_msg'],
    "type":1
}
addPeoDetial_req = requests.post(url=addPeo_detial,cookies = creatCookie,data=addPeoDetial_data)
print(addPeoDetial_req.json())
'''
#登记授予期权
'''
issue_equity_url = "https://test.kapbook.cn/equity/company/issue_equity_ajax"
issue_equity_data = {
    "step": "2",
    "certificate_id": "",
    "plan_id": "3242",
    "group_id": "0",
    "option_grant_type": "1",
    "issue_type": "2",
    "model_type": "existingPlan",
    "is_show_vesting": "0",
    "amtExceed": "true",
    "company_user_id": "33891",
    "option_grant_model": "undefined",
    "amount": "100",
    "hold_company_user_id": "undefined",
    "issue_date": "2020-12-01",
    "exercise_price": "0.10",
    "back_price_type": "2",
    "back_price_amount": "0",
    "is_scheme_custom": "0",
    "vesting_schedule_id": "0",
    "vesting_start_date": "2020-12-01",
    "vesting_date_undefined": "",
    "accelerate_is_provision": "0",
    "accelerate_provision": "",
    "supplemental": "0",
    "other_constraint": "",
    "pay_type": "0",
    "is_upload_voucher": "undefined",
    "document_path_9": "undefined",
    "document_path_1": "",
    "notes": ""
}
issue_equity_response = requests.post(url=issue_equity_url,cookies=creatCookie,data=issue_equity_data)
print(issue_equity_response.json())
'''


#添加公司列表
'''
company_data ={
    "company_id": "undefined",
    "company_type": "",
    "currency": "",
    "full_name": "测试有限公司",
    "company_name": "测试有限公司",
    "document_path": "undefined",
    "is_version": 'null',
}
company_res = requests.post(url=Save_company, cookies=cookie, data=company_data)
print(company_res.json())
'''

#添加计划返回数据信息 data=6fb0cafd25e00d0df8d174a3c5fdb4ba
'''
{
    "plan_name":"\u80a1\u6743\u6fc0\u52b1\u8ba1\u5212",
    "company_name":"\u6d4b\u8bd5\u6709\u9650\u516c\u53f8test2",
    "legal_person":null,
    "userList":{
        "1":[
            {"id":"33907",
             "name":"15028217377",
             "email":"--",
             "company_user_type":"1",
             "status":"3",
             "uid":"686",
             "role":"1",
             "nationcode_id":"214",
             "nationcode":"86",
             "phone":"--",
             "address":"--",
             "native_place":"--",
             "english_name":"--",
             "position":"--",
             "is_investor":"0",
             "board_type":"0",
             "department":"--",
             "full_name":"--",
             "certificate_type":"1",
             "certificate_code":"--",
             "id_no":"--",
             "is_inside":"0",
             "dimission":"0",
             "is_rule":"0",
             "is_affiliate":"0",
             "country_id":"--",
             "first_name":"--",
             "last_name":"--",
             "profession_no":"--",
             "birth_date":"0000-00-00",
             "sex":"--",
             "entry_date":"0000-00-00",
             "tax_code":"--",
             "is_safe":"0",
             "is_trader":"0",
             "is_admin":"0",
             "is_dimission":"0",
             "pay_taxes_id":"1",
             "wage":"0.00",
             "city_name":"\u5317\u4eac\u5e02",
             "province_id":"1",
             "country_name":"--",
             "custom_info":"--",
             "level":"--",
             "platform_type":"--",
             "city_list":"--",
             "is_complete":0,
             "type":"\u975e\u6295\u8d44\u4eba","emailfull":"--"
             }
        ],
        "9":[]},
    "vesting_schedule_id":"<option value=28898>1\/48\u4e2a\u6708\uff0c12\u4e2a\u6708\u9501\u5b9a\u671f<\/option>"
                          "<option value=28899>1\/4\u5e74\uff0c\u65e0\u9501\u5b9a\u671f<\/option>"
                          "<option value=28900>1\/48\u4e2a\u6708\uff0c\u65e0\u9501\u5b9a\u671f<\/option>",
    "buybackDefaultInfo":{
        "1":"\u88ab\u6388\u4e88\u4eba\u56e0\u6545\u610f\u6216\u91cd\u5927\u8fc7\u5931\u884c\u4e3a\uff0c\u4e25\u91cd\u8fdd\u53cd\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u7684\u89c4\u7ae0\u5236\u5ea6\u3001\u52b3\u52a8\u5408\u540c\/\u987e\u95ee\u670d\u52a1\u534f\u8bae\u6216\u6709\u5176\u4ed6\u4e25\u91cd\u4e0d\u5f53\u884c\u4e3a\uff0c\u4f7f\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u906d\u53d7\u91cd\u5927\u635f\u5931\u6216\u8005\u635f\u5bb3\u7684\uff1b",
        "2":"\u88ab\u6388\u4e88\u4eba\u56e0\u9488\u5bf9\u516c\u53f8\u6216\u5173\u8054\u516c\u53f8\u7684\u4e0d\u5f53\u884c\u4e3a\u800c\u6784\u6210\u5211\u4e8b\u72af\u7f6a\u7684\uff1b",
        "3":"\u88ab\u6388\u4e88\u4eba\u8fdd\u53cd\u672c\u534f\u8bae\u7b2c7.2\u6761\u4fdd\u5bc6\u4e49\u52a1\u53ca\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u7684\u5546\u4e1a\u79d8\u5bc6\u7684\uff1b",
        "4":"\u88ab\u6388\u4e88\u4eba\u8fdd\u53cd\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u5173\u4e8e\u53cd\u8150\u8d25\u53ca\u53cd\u5546\u4e1a\u8d3f\u8d42\u7684\u5185\u90e8\u5236\u5ea6\u7684\uff1b",
        "5":"\u88ab\u6388\u4e88\u4eba\u8fdd\u53cd\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u7684\u7ade\u4e1a\u7981\u6b62\u3001\u7981\u6b62\u529d\u8bf1\u4e49\u52a1\u7684\uff1b",
        "6":"\u88ab\u6388\u4e88\u4eba\u5728\u5176\u4efb\u804c\/\u63d0\u4f9b\u987e\u95ee\u670d\u52a1\u671f\u95f4\u6216\u8005\u79bb\u804c\/\u7ec8\u6b62\u987e\u95ee\u670d\u52a1\u540e\u5177\u6709\u5bf9\u516c\u53f8\u6216\u5176\u5173\u8054\u516c\u53f8\u7684\u4e0d\u6b63\u5f53\u7ade\u4e89\u884c\u4e3a\u6216\u5728\u516c\u5171\u573a\u5408\u6216\u901a\u8fc7\u5176\u4ed6\u516c\u5171\u6e20\u9053\u6545\u610f\u8bcb\u6bc1\u516c\u53f8\u58f0\u8a89\u3001\u6563\u5e03\u4e0d\u5229\u4e8e\u516c\u53f8\u7684\u8a00\u8bba\u6216\u6709\u5176\u4ed6\u6c61\u8511\u3001\u8bfd\u8c24\u516c\u53f8\u7684\u884c\u4e3a\u3002"},
    "uploadbtnArr":{
        "1":"EIP(\u80a1\u6743\u6fc0\u52b1\u8ba1\u5212)"},
    "signInitializeaArr":{"1":{"list":[{"sign_param_id":301,"nickname":"\u6fc0\u52b1\u5bf9\u8c61\u7b7e\u5b57","epsp_name":"\u6fc0\u52b1\u5bf9\u8c61\u7b7e\u5b57","is_radio":0,"format":1,"signx":0,"signy":0,"signdatex":0,"signdatey":0,"type":3,"branch":1}],"name":"\u6fc0\u52b1\u5bf9\u8c61\u7b7e\u5b57"},
                          "2":{"list":[{"sign_param_id":601,"nickname":"\u51fa\u8ba9\u65b9\u7b7e\u5b57","epsp_name":"\u51fa\u8ba9\u65b9\u7b7e\u5b57","is_radio":0,"format":1,"signx":0,"signy":0,"signdatex":0,"signdatey":0,"type":6,"branch":1}],"name":"\u51fa\u8ba9\u65b9\u7b7e\u5b57"},
                          "3":{"list":[{"sign_param_id":103,"nickname":"\u516c\u53f8\u76d6\u7ae0","epsp_name":"\u516c\u53f8\u76d6\u7ae0","is_radio":2,"format":2,"signx":0,"signy":0,"signdatex":0,"signdatey":0,"type":1,"branch":1},{"sign_param_id":102,"nickname":"\u6388\u6743\u4ee3\u8868\u7b7e\u5b57","epsp_name":"\u6388\u6743\u4ee3\u8868\u7b7e\u5b57","is_radio":2,"format":1,"signx":0,"signy":0,"signdatex":0,"signdatey":0,"type":1,"branch":1}],"name":"\u6388\u4e88\u4eba\u8bbe\u7f6e(\u81f3\u5c11\u9009\u62e9\u4e00\u9879)"}},
    "financing_stage":{
        "1":"\u5c1a\u672a\u83b7\u6295",#尚未获取
        "2":"\u79cd\u5b50\u8f6e",
        "3":"\u5929\u4f7f\u8f6e",
        "4":"Pre-A\u8f6e",
        "5":"A\u8f6e",
        "6":"A+\u8f6e",
        "7":"Pre-B\u8f6e",
        "8":"B\u8f6e",
        "9":"B+\u8f6e","10":"C\u8f6e","11":"D\u8f6e","12":"E\u8f6e","13":"F\u8f6e-\u4e0a\u5e02\u524d","14":"\u5176\u4ed6"},
    "exercise_retention_type_arr":{
        "1":"\u5e74","2":"\u6708","3":"\u5929"},
    "exerciseArr":{
        "401":{"branch":2,"sign_format":1,"sign_property_id":"401","sort":1,"type":4,"nickname":"\u53d7\u8ba9\u65b9"},
        "501":{"branch":2,"sign_format":1,"sign_property_id":"501","sort":2,"type":5,"nickname":"\u51fa\u8ba9\u65b9"}},
    "exercise_window_type_arr":
        [
            {"key":4,"value":"\u6682\u4e0d\u5f00\u653e"},#暂不开放
            {"key":1,"value":"\u968f\u65f6"},
            {"key":2,"value":"\u6bcf\u5e74\u4e00\u6b21"},
            {"key":3,"value":"\u6bcf\u6708\u4e00\u6b21"},
            {"key":5,"value":"\u6bcf\u5e74\u591a\u6b21\u81ea\u5b9a\u4e49\u65f6\u95f4\u6bb5"}
        ],
    "regist_capital":"0","fair_value":"","company_financing_stage_id":"","is_update_company_regist_capital":1};

'''



