from selenium.webdriver.common.by import By
from PO import base_page


class HoldplatformPage(base_page.Action):
    company_man = (By.CSS_SELECTOR, ".Kap_only_Menus li:nth-child(5) .navTitle")  # 公司管理
    hold_platform_select = (By.CSS_SELECTOR, ".Kap_only_Menus li:last-child  .navChildren  p:nth-child(2)")#持股平台
    add_platform = (By.ID, "addPlatformSelect")  #添加持股平台
    single_platform = (By.CSS_SELECTOR, "#addPlatformSelect li:first-child") #单层持股平台添加
    platform_name = (By.ID, "platformName")  #名称
    platform_type = (By.ID, "platformType") #公司类型
    liability_com = (By.CSS_SELECTOR, "#platformType li:first-child")  #有限责任公司
    partnership_com = (By.CSS_SELECTOR, "#platformType li:last-child") #有限合伙企业
    platform_captical = (By.ID, "platformCapital")  #注册资本
    platform_Shares =(By.ID, "platformShares")#持有公司注册资本
    platformBtnStep1 = (By.ID, "platformBtnStep1")  # 下一步按钮
    addplatform_tr = (By.ID, "addplatform_tr") #添加股东
    platform_tr_name1 = (By.CSS_SELECTOR, ".platform_tr_name1")  #添加第一个股东姓名
    first_shareholders = (By.CSS_SELECTOR, ".search_user_list tr:nth-child(1)")  #第一个股东选择
    memberShare = (By.ID, "memberShare") #注册资本添加
    memberSharePay = (By.ID, "memberSharePay")#实缴金额
    platformMemInfoClose = (By.ID, "platformMemInfoClose")#注册资本页取消
    platformMemInfoSubmit = (By.ID, "platformMemInfoSubmit") #注册资本确定
    platform_tr_name2 = (By.CSS_SELECTOR, ".platform_tr_name2")  #添加第二个股东姓名
    second_shareholders = (By.CSS_SELECTOR, ".search_user_list tr:nth-child(2)")  # 第二个股东选择
    platformLastStep2 = (By.ID, "platformLastStep2")  #上一步按钮
    platformBtnStep2 = (By.ID, "platformBtnStep2")  # 下一步按钮
    platform_transferor = (By.ID, "platform_transferor")  # 代持人选择框
    transferor_select = (By.CSS_SELECTOR, "#platform_transferor li:nth-child(1)")  #代持人选择
    inputMaxTransferShare = (By.ID, "inputMaxTransferShare")  # 股权激励注册资本
    platformLastStep3 = (By.ID, "platformLastStep3")  # 上一步按钮
    platformBtnStep3 = (By.ID, "platformBtnStep3")  # 下一步按钮
    bankUserName = (By.ID, "bankUserName")  # 户名
    bankName = (By.ID, "bankName") #开户行
    inputBankNum = (By.ID, "inputBankNum")  # 账号
    platformLastStep4 = (By.ID, "platformLastStep4")  # 上一步按钮
    platformBtnStep4 = (By.ID, "platformBtnStep4")  # 下一步按钮
    jump_this_step = (By.CSS_SELECTOR, ".jump_this_step")  # 跳过此步骤
    platformLastStep5 = (By.ID, "platformLastStep5")  # 返回修改
    platformBtnStep5 = (By.ID, "platformBtnStep5")  # 提交确认按钮
    alert_Iknow = (By.CSS_SELECTOR, "#common_alert .btn.alert_btn_yes") #我知道了弹出框关闭
    #提示信息
    firName_text = (By.CSS_SELECTOR, "#platformName +em")#名称提示
    firCapital_text = (By.CSS_SELECTOR, "#platformCapital~em")  #注册资本
    firShares_text = (By.CSS_SELECTOR, "#lookupPlatformStructure~em")  #持有注册资本
    firAlert_company = (By.CSS_SELECTOR, "#common_alert p")  #名称相同弹出框文案获取
    firAlert_company = (By.CSS_SELECTOR, "#common_alert .alert_btn_yes")  #弹出框确定按钮
    sec_memberShare = (By.CSS_SELECTOR, "#memberShare~em")  #  注册资本输入框
    sec_memberSharePay = (By.CSS_SELECTOR, "#memberSharePay~em")  # 实缴金额输入框
     # = (, "")  #~

    #创建完操作步骤
    tableBtnserach = (By.CSS_SELECTOR, ".platform_tab_content>div>div:nth-child(1) .searchBtn") #操作
    set_draftBth_select =(By.CSS_SELECTOR, ".platform_tab_content>div>div:nth-child(1) .set_platform_draft_Btn") #设为草稿选择
    set_draftBth_btn =(By.CSS_SELECTOR, "#common_alert .btn.alert_btn_yes") #设为草稿btn
    checkProgressBtn = (By.CSS_SELECTOR, ".platform_tab_content>div>div:nth-child(1) .platform_checkProgress_Btn")  # 查看进度
    upload_Btn = (By.CSS_SELECTOR, ".platform_tab_content>div>div:nth-child(1) .att_upload_btn")  # 上传附件

    #草稿状态
    del_platform = (By.CSS_SELECTOR, ".platform_tab_content>div>div:nth-child(1) .del_platform_Btn") #删除按钮
    del_platform_yes = (By.CSS_SELECTOR, "#common_alert .alert_btn_yes") #确定删除

    def op_move(self, obj):
        if obj == "公司管理":
            return self.Act

            ionChains(*self.company_man)
        # elif obj == "预览-确定":
        #     ele1 = self.find_element(self.platformBtnStep5)
        #     self.script(ele1)
        #     ele1.click()
        elif obj == "预览-确定":
            ele1 = self.find_element(*self.platformBtnStep5)
            return ele1

    def op_click(self, obj):
        if obj == "持股平台":
            self.find_element(*self.hold_platform_select).click()
        elif obj == "公司管理":
            self.find_element(*self.company_man).click()
        elif obj == "添加持股平台":
            self.find_element(*self.add_platform).click()
        elif obj == "单层持股平台":
            self.find_element(*self.single_platform).click()
        elif obj == "基本信息-下一步":
            self.find_element(*self.platformBtnStep1).click()
        elif obj == "添加股东btn":
            self.find_element(*self.addplatform_tr).click()
        elif obj == "注册资本页-确定":
            self.find_element(*self.platformMemInfoSubmit).click()
        elif obj == "股权信息-下一步":
            self.find_element(*self.platformBtnStep2).click()
        elif obj == "代持人-下一步":
            self.find_element(*self.platformBtnStep3).click()
        elif obj == "对公账户-下一步":
            self.find_element(*self.platformBtnStep4).click()
        elif obj == "我知道了":
            self.find_element(*self.alert_Iknow).click()
        elif obj == "操作":
            self.find_element(*self.tableBtnserach).click()
        elif obj == "设为草稿select":
            self.find_element(*self.set_draftBth_select).click()
        elif obj == "设为草稿btn":
            self.find_element(*self.set_draftBth_btn).click()
        elif obj == "删除持股平台":
            self.find_element(*self.del_platform).click()
            self.find_element(*self.del_platform_yes).click()
        elif obj == "fir弹出框btn":     #弹出框提示关闭按钮
            self.find_element(*self. firAlert_company).click()


    def op_input(self, obj , string):
        if obj == "公司名称":
            self.send_keys(self.platform_name, string)
        elif obj == "基本信息-注册资本":
            self.send_keys(self.platform_captical, string)
        elif obj == "基本信息-持有资本":
            self.send_keys(self.platform_Shares, string)
        elif obj == "注册资本":
            self.send_keys(self.memberShare, string)
        elif obj == "实缴金额":
            self.send_keys(self.memberSharePay, string)
        elif obj == "代持人-注册资本":
            self.send_keys(self.inputMaxTransferShare, string)
        elif obj == "对公账户-开户行":
            self.send_keys(self.bankName, string)
        elif obj == "对公账户-账号":
            self.send_keys(self.inputBankNum, string)


    def op_select(self, obj):
        if obj == "公司类型-责任":
            self.find_element(*self.platform_type).click()
            self.find_element(*self.liability_com).click()
        elif obj == "first股东添加":
            self.find_element(*self.platform_tr_name1).click()
            self.find_element(*self.first_shareholders).click()
        elif obj == "second股东添加":
            self.find_element(*self.platform_tr_name2).click()
            self.find_element(*self.second_shareholders).click()
        elif obj == "代持人-代持人sel":
            self.find_element(*self.platform_transferor).click()
            self.find_element(*self.transferor_select).click()

    def show_alert(self, obj):
        if obj == "名称文本提示":
            return self.find_element(*self.firName_text).text
        elif obj == "注册资本提示":
            return self.find_element(*self.firCapital_text).text
        elif obj == "持有资本提示":
            return self.find_element(*self.firShares_text).text
        elif obj == "弹出框提示":
            return self.find_element(*self.firAlert_company).text
        elif obj == "sec注册资本text":
            return self.find_element(*self.sec_memberShare).text
        elif obj == "sec实缴金额text":
            return self.find_element(*self.sec_memberSharePay).text


















