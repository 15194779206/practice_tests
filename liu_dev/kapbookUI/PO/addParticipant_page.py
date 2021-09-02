from selenium.webdriver.common.by import By
from PO import base_page
'''
添加参与方
前提条件：
1：
'''

class ParticipantPage(base_page.Action):
    company_man = (By.CSS_SELECTOR, ".Kap_only_Menus li:nth-child(5) .navTitle") #公司管理
    add_people = (By.ID, "addPeople")   #添加参与方
    list_title = (By.CSS_SELECTOR, "#setPeopleAlert .alert_title .fl") #头标题
    nature_people = (By.CSS_SELECTOR, ".cont_title>div:nth-child(2) div")  #自然人
    Legal_people = (By.CSS_SELECTOR, ".cont_title>div:nth-child(3) div")  #法人
    name = (By.ID, "natural_name")   #姓名
    email = (By.ID, "natural_email") #邮箱
    certificate_type = (By.ID, "natural_certificate_type") #证件选择框
    certificate_choose1 = (By.CSS_SELECTOR, "#natural_certificate_type li:nth-child(1)")   #证件号选择第一个框
    certificate_choose2 = (By.CSS_SELECTOR, "#natural_certificate_type li:nth-child(2)")   #证件号选择第二个框
    certificate_choose3 = (By.CSS_SELECTOR, "#natural_certificate_type li:nth-child(3)")  # 证件号选择第三个框
    certificate_choose4 = (By.CSS_SELECTOR, "#natural_certificate_type li:nth-child(4)")  # 证件号选择第四个框
    certificate = (By.ID, "natural_certificate_code")   #证件号输入框 
    access_permission = (By.ID, "addstatementAccess")  #访问权限下拉框
    permission_None = (By.CSS_SELECTOR, "#addstatementAccess li:nth-child(1)")  #权限无
    permission_Man = (By.CSS_SELECTOR, "#addstatementAccess li:nth-child(2)")   #权限管理员
    permission_Custom = (By.CSS_SELECTOR, "#addstatementAccess li:nth-child(3)") #权限自定义
    board_Manager = (By.ID, "addstatementBool")  #董事会管理员复选框
    director_people = (By.CSS_SELECTOR, ".isBossDiv.mb5>div:nth-child(2) div")  #董事
    Observers_people = (By.CSS_SELECTOR, ".isBossDiv.mb5>div:nth-child(3) div")  #观察员
    send_email = (By.CSS_SELECTOR, ".checkYes.emailBok")  #发送邮件复选框
    determine = (By.CSS_SELECTOR, "#setPeopleAlert>div:nth-child(3)>.alert_btn_yes")  #确定按钮

    #法人模块#setPeopleAlert>div:nth-child(3)>a:nth-child(2)
    company_mane = (By.ID, "legalName")  # 企业名称
    header_name = (By.ID, "legalPeople")  # 负责人姓名
    name_select = (By.CSS_SELECTOR, ".searchDiv  .oa ul:nth-child(2)")  #选择负责人
    credit_code= (By.ID, "legalCode")  # 统一社会信用代码
    license_img = (By.ID, "upload_backgroundImage")  #营业执照上传图片
    company_btn = (By.CSS_SELECTOR, "#setPeopleAlert .btn.minbtn.alert_btn_yes")  # 确定按钮

    #删除操作
    editor = (By.CSS_SELECTOR, "#managerTableId tr:nth-child(2) .edit_people")  #编辑按钮
    delete = (By.CSS_SELECTOR, ".del_btn")    #删除按钮
    delete_cho = (By.CSS_SELECTOR, "#common_alert>div:nth-child(3)>.alert_btn_yes")  #弹出框确认删除
    sProgram_button = (By.CSS_SELECTOR, "#proceInvitation .alert_btn_yes") #小程序按钮添加成功弹出框

    #判断
    data_first_id = (By.CSS_SELECTOR, "#managerTableId tr:nth-child(1)")   #获取第一条数据，用户获取data
    data_first_infos = (By.CSS_SELECTOR, "#managerTableId tr:nth-child(1) td")#获取第一条数据
    data_titles_row = (By.CSS_SELECTOR, "#plan_table_fixed th")  #获取标题

    #提示信息部分
    name_text = (By.CSS_SELECTOR, "#natural_name+.red")   #姓名为空提示
    email_text = (By.CSS_SELECTOR, "#natural_email+.red")    #邮箱为空提示
    certificate_text = (By.CSS_SELECTOR, "#natural_certificate_code+.red")  #证件号为空提示
    titleTips_text = (By.CSS_SELECTOR, "#setPeopleAlert .tips .tips_list span:nth-child(2)")   #头部信息栏提示

    #获取所有的姓名
    name_list = (By.CSS_SELECTOR, "#managerTableId  td:nth-child(2)")
    mail_list = (By.CSS_SELECTOR, "#managerTableId  td:nth-child(3)")

    #法人部分信息提示
    legalName = (By.CSS_SELECTOR, "#legalName+.red")  #企业名称
    legalPeople = (By.CSS_SELECTOR, "#legalPeople+div+em.red")  #负责人姓名
    legalCode = (By.CSS_SELECTOR, "#legalCode +em.red")  #社会代码

    def op_click(self, obj):
        if obj == "公司管理":
            self.find_element(*self.company_man).click()
        elif obj == "添加参与方":
            self.find_element(*self.add_people).click()
        elif obj == "确定":
            self.find_element(*self.determine).click()
        elif obj == "编辑":
            self.find_element(*self.editor).click()
        elif obj == "删除":
            self.find_element(*self.delete).click()
        elif obj == "确定_删除":
            self.find_element(*self.delete_cho).click()
        elif obj == "小程序确定Btn":
            self.find_element(*self.sProgram_button).click()
        elif obj == "自然人radio":
            self.find_element(*self.nature_people).click()
        elif obj == "法人radio":
            self.find_element(*self.Legal_people).click()
        elif obj == "负责人姓名":
            self.find_element(*self.header_name).click()
            self.find_element(*self.name_select).click()
        elif obj == "执照上传":
            self.find_element(*self.license_img).click()
        elif obj == "法人确定添加":
            self.find_element(*self.company_btn).click()
        elif obj == "营业执照":
            self.find_element(*self.license_img).click()

    def op_select(self, obj, string):
        if obj == "证件类型" and string == "身份证":
            self.find_element(*self.certificate_type).click()
            self.find_element(*self.certificate_choose1).click()
        elif obj == "证件类型" and string == "护照":
            self.find_element(*self.certificate_type).click()
            self.find_element(*self.certificate_choose2).click()
        elif obj == "证件类型" and string == "台胞证":
            self.find_element(*self.certificate_type).click()
            self.find_element(*self.certificate_choose3).click()
        elif obj == "证件类型" and string == "回乡证":
            self.find_element(*self.certificate_type).click()
            self.find_element(*self.certificate_choose4).click()



    def op_input(self, obj, string):
        if obj == "姓名":
            self.send_keys(self.name, string)
        elif obj == "邮箱":
            self.send_keys(self.email, string)
        elif obj == "证件号":
            self.send_keys(self.certificate, string)
        elif obj == "企业名称":
            self.send_keys(self.company_mane, string)
        elif obj == "信用代码":
            self.send_keys(self.credit_code, string)


    def show_alert(self, obj):
        if obj == "姓名提示":
            return self.find_element(*self.name_text).text
        elif obj == "邮箱提示":
            return self.find_element(*self.email_text).text
        elif obj == "证件提示":
            return self.find_element(*self.certificate_text).text
        elif obj == "title栏提示":
            return self.find_element(*self.titleTips_text).text
        elif obj == "企业名称提示":
            return self.find_element(*self.legalName).text
        elif obj == "负责人提示":
            return self.find_element(*self.legalPeople).text
        elif obj == "社会代码提示":
            return self.find_element(*self.legalCode).text



    def op_check(self, obj):
        if obj == "第1条数据":
            infos = [self.find_element(*self.data_first_id).get_attribute('data')]
            titles = ['id']
            infos_list = self.find_elements(*self.data_first_infos)  #获取第一条数据
            titles_list = self.find_elements(*self.data_titles_row)
            for i in range(1, len(titles_list)-1):
                infos.append(infos_list[i].text.strip(' ').replace('\n', '~'))
                titles.append(titles_list[i].text.strip(' ').replace('\n', '~'))
            data = dict(zip(titles, infos))   #返回字典
            print('第一条数据', data)#{'id': '31330', '参与方名称': '授予人1', '邮箱': 'lyangluck@126.com', '状态': '已确认', '员工ID': '--', '部门': '--', '权限': '无'}
            return data
        elif obj == "姓名和邮箱已存在":
            infos = []
            titles = []
            name_list = self.find_elements(*self.name_list)
            mail_list = self.find_elements(*self.mail_list)
            for i in range(0, len(name_list)):
                titles.append(name_list[i].text.strip(' ').replace('\n', '~'))
                infos.append(mail_list[i].text.strip(' ').replace('\n', '~'))
            data = dict(zip(titles, infos))  # 返回字典
            print('姓名', data)
            return data
        #elif obj == "":



