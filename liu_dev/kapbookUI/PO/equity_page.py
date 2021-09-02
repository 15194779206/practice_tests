from selenium.webdriver.common.by import By
from PO import base_page


class EquityPage(base_page.Action):
    view_RS = (By.CSS_SELECTOR, ".topMenusDiv .bubbleDiv a:nth-child(2)")
    view_equity = (By.CSS_SELECTOR, ".topMenusDiv .bubbleDiv a:nth-child(1)")
    btn_give = (By.CSS_SELECTOR, "#equityBtns")
    list_singleGive = (By.CSS_SELECTOR, "#equityBtns .equityDivBtn")
    list_plan = (By.CSS_SELECTOR, ".planSelect")
    list_planOption = (By.CSS_SELECTOR, ".planSelect ul > li:nth-child(1)")
    list_giveCatagrate = (By.CSS_SELECTOR, ".equitySelect")
    list_giveCatagrateOption = (By.CSS_SELECTOR, ".equitySelect ul > li:nth-child(1)")
    list_giveCatagrateStock = (By.CSS_SELECTOR, ".equitySelect ul > li:nth-child(2)")
    list_template = (By.CSS_SELECTOR, ".templateSelect")
    list_templateOption = (By.CSS_SELECTOR, ".templateSelect ul > li:nth-child(1)")
    btn_first_next = (By.CSS_SELECTOR, ".equityDiv_1 .alert_btn_box > a")

    input_name = (By.CSS_SELECTOR, "input.company_user_name")
    list_name = (By.CSS_SELECTOR, ".search_user_list tr:nth-child(1)")
    input_amount = (By.CSS_SELECTOR, ".eAmount")
    btn_amountClose = (By.CSS_SELECTOR, ".eAmount ~ .addoption_page_amountDiv .losspan")
    input_holder = (By.CSS_SELECTOR, "input.platform_name")
    input_giveDate = (By.CSS_SELECTOR, ".eDate")
    icon_giveDate = (By.CSS_SELECTOR, ".eDate  + i span")
    input_exercisePrice = (By.CSS_SELECTOR, ".ePrice")
    btn_exercisePriceClose = (By.CSS_SELECTOR, '.ePrice ~  .addoption_page_amountDiv .losspan')
    checkbox_callbackPrice = (By.CSS_SELECTOR, ".callbackPriceDiv dd:nth-child(2)")
    list_maturePlan = (By.CSS_SELECTOR, "div.maturePlan")
    list_maturePlanOption = (By.CSS_SELECTOR, "div.maturePlan li:nth-child(2)")
    input_vestingDate = (By.CSS_SELECTOR, ".eMatureDate")
    icon_vestingDate = (By.CSS_SELECTOR, ".eMatureDate  + i span")
    btn_second_next = (By.CSS_SELECTOR, ".equityDiv_2 .alert_btn_box .alert_btn_yes")

    btn_third_next = (By.CSS_SELECTOR, ".equityDiv_3 .alert_btn_box .alert_btn_yes")

    btn_opList = (By.CSS_SELECTOR, "#plan_table tr:nth-child(1) .searchBtn")
    list_delete = (By.CSS_SELECTOR, "#plan_table tr:nth-child(1) .del_option")

    btn_confirm = (By.CSS_SELECTOR, "#del_optionDiv .confirm_yes")

    data_first_id = (By.CSS_SELECTOR, "#plan_table tr:nth-child(1)")
    data_first_infos = (By.CSS_SELECTOR, "#plan_table tr:nth-child(1) td")
    data_titles_row = (By.CSS_SELECTOR, "#plan_table_fixed th")


    def op_click(self, obj):
        if obj == '期权':
            self.find_element(*self.view_equity).click()
        elif obj == '受限股':
            self.find_element(*self.view_RS).click()
        elif obj == '授予':
            self.find_element(*self.btn_give).click()
        elif obj == '第1步-下一步':
            self.find_element(*self.btn_first_next).click()
        elif obj == '第2步-下一步':
            self.find_element(*self.btn_second_next).click()
        elif obj == '完成':
            self.find_element(*self.btn_third_next).click()
        elif obj == '操作':
            self.find_element(*self.btn_opList).click()
        elif obj == '确认删除':
            self.find_element(*self.btn_confirm).click()

    def op_select(self, obj):
        if obj == '单人授予':
            self.find_element(*self.list_singleGive).click()
        elif obj == '激励计划':
            self.find_element(*self.list_plan).click()
            self.find_element(*self.list_planOption).click()
        elif obj == '授予类型-期权':
            self.find_element(*self.list_giveCatagrate).click()
            self.find_element(*self.list_giveCatagrateOption).click()
        elif obj == '授予类型-受限股':
            self.find_element(*self.list_giveCatagrate).click()
            self.find_element(*self.list_giveCatagrateStock).click()
        elif obj == '协议模板-系统模板':
            self.find_element(*self.list_template).click()
            self.find_element(*self.list_templateOption).click()
        elif obj == '姓名':
            self.find_element(*self.input_name).click()
            self.find_element(*self.list_name).click()
        elif obj == '代持股东':
            self.find_element(*self.input_holder).click()
            self.find_element(*self.list_name).click()
        elif obj == '回购价格':
            self.find_element(*self.checkbox_callbackPrice).click()
        elif obj == '成熟计划' or obj == '解限计划':
            self.find_element(*self.list_maturePlan).click()
            self.find_element(*self.list_maturePlanOption).click()
        elif obj == '删除草稿':
            self.find_element(*self.list_delete).click()

    def op_input(self, obj, string):
        if obj == '数量':
            self.send_keys(self.input_amount, string)
            self.find_element(*self.btn_amountClose).click()
        elif obj == '授予日期':
            js = "$('" + self.input_giveDate[1] + "').removeAttr('readonly')"
            self.script(js)
            self.send_keys(self.input_giveDate, string)
            self.find_element(*self.icon_giveDate).click()
        elif obj == '行权单价':
            self.send_keys(self.input_exercisePrice, string)
            self.find_element(*self.btn_exercisePriceClose).click()
        elif obj == '成熟起算日' or obj == '解限起算日':
            js = "$('" + self.input_vestingDate[1] + "').removeAttr('readonly')"
            self.script(js)
            self.send_keys(self.input_vestingDate, string)
            self.find_element(*self.icon_vestingDate).click()

    def op_check(self, obj):
        if obj == '第1条数据':
            infos = [self.find_element(*self.data_first_id).get_attribute('data')]
            titles = ['id']
            infos_list = self.find_elements(*self.data_first_infos)  #获取第一条数据
            titles_list = self.find_elements(*self.data_titles_row)  #获取标题
            print(len(titles_list))
            for n in range(1, len(titles_list) - 1):
                infos.append(infos_list[n].text.strip(' ').replace('\n', '~'))
                titles.append(titles_list[n].text.strip(' ').replace('\n', '~'))
            data = dict(zip(titles, infos))
            print(data)
            return data
