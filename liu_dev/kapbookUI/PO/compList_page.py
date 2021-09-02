from selenium.webdriver.common.by import By

from PO import base_page


class CompListPage(base_page.Action):
    logo_index = (By.CSS_SELECTOR, ".Kap_only_Menus .topbar_logo")
    link_create = (By.CSS_SELECTOR, ".newCompanyA")
    icon_msg = (By.CSS_SELECTOR, ".Kap_only_Menus .topbar_Ico")
    icon_num = (By.CSS_SELECTOR, ".Kap_only_Menus .topbar_Num")
    menu_support = (By.CSS_SELECTOR, ".Kap_only_Menus .help_title")
    menu_user = (By.CSS_SELECTOR, ".Kap_only_Menus .topbar_user")
    navi_list = (By.CSS_SELECTOR, ".Kap_only_Menus .navTitle")
    navi_complist = (By.CSS_SELECTOR, ".Kap_only_Menus .companyIco + div")
    navi_info = (By.CSS_SELECTOR, ".Kap_only_Menus .userIco + div")
    navi_property = (By.CSS_SELECTOR, ".Kap_only_Menus .assetsIco + div")
    navi_pending = (By.CSS_SELECTOR, ".Kap_only_Menus .propertyIco + div")
    navi_bill = (By.CSS_SELECTOR, ".Kap_only_Menus .billIco + div")
    navi_msg = (By.CSS_SELECTOR, ".Kap_only_Menus .systemIco + div")
    list_help = (By.CSS_SELECTOR, ".Kap_only_Menus .helpBtn")
    list_feedback = (By.CSS_SELECTOR, ".Kap_only_Menus .user_top_feedback")
    list_service = (By.ID, "user_service")
    list_userinfo = (By.CSS_SELECTOR, ".Kap_only_Menus .userinfoBtn")
    list_property = (By.CSS_SELECTOR, ".Kap_only_Menus .topbarmymoneyIcon")
    list_logout = (By.CSS_SELECTOR, ".Kap_only_Menus .topbaroutIcon")
    banner_info = (By.CSS_SELECTOR, "#Prompt_Auth .Prompt_Auth_text")
    banner_num = (By.CSS_SELECTOR, "#Prompt_Auth .Prompt_Auth_text span")
    text_name = (By.CSS_SELECTOR, ".Kap_only_Menus .topbar_user div")
    comp_name = (By.CSS_SELECTOR, ".enterpListName")

    def op_click(self, obj):
        if obj == '页面LOGO':
            self.find_element(*self.logo_index).click()
        elif obj == '退出登录':
            self.find_element(*self.list_logout).click()
        elif obj == '第一个企业有限公司':
            for name in self.find_elements(*self.comp_name):
                if name.get_attribute('title') == obj:
                    name.click()

    def show_text(self, obj):
        if obj == '当前用户姓名':
            try:
                self.name = self.find_element(*self.text_name).text.split('，')[1]
            except Exception as e:
                self.name = self.find_element(*self.text_name)
            return self.name
        elif obj == '消息图标未读数量':
            try:
                self.num = self.find_element(*self.icon_num).text
            except Exception as e:
                self.num = self.find_element(*self.text_name)
            return self.num
        elif obj == 'banner提示':
            try:
                self.banner_num = self.find_element(*self.banner_num).text
            except Exception as e:
                self.banner_num = self.find_element(*self.banner_num)
            return self.banner_num
        elif obj == '导航菜单':
            menuList = []
            try:
                for navi in self.find_elements(*self.navi_list):
                    menuList.append(navi.text)
            except Exception as e:
                menuList.append(self.find_elements(*self.navi_list))
            return menuList

    def mouse_suspension(self, obj):
        if obj == '技术支持':
            self.ActionChains(*self.menu_support)
        elif obj == '当前用户姓名':
            self.ActionChains(*self.menu_user)
