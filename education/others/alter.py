from selenium import webdriver
brower=webdriver.Chrome()
# 用于删除点击确定和删除的应用
brower.get('http://admin.jiajiabank.com/admin/operatingcenter')
dele=brower.find_element_by_xpath('/html/body/div/div[2]/div/section/section/main/div/div[2]/div[2]/div[1]/div/span[3]')
dele.click();
alter=dele.switch_to_alert();
alter.dismiss()