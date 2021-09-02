from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://test.kapbook.cn')

driver.find_element_by_id('email').send_keys('liuyitong@kapbook.com')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('login_ajax').click()

driver.find_element_by_css_selector('.enterpList .enterpListDiv:nth-child(12)').click()

first_id = driver.find_element_by_css_selector('#plan_table tr:nth-child(1)').get_attribute('data')
first_info = driver.find_elements_by_css_selector('#plan_table tr:nth-child(1) td')
titles_info = driver.find_elements_by_css_selector('#plan_table_fixed th')
infos = [first_id]
titles = ['id']
for n in range(1, len(titles_info)-1):
    infos.append(first_info[n].text.strip(' ').replace('\n', '~'))
    titles.append(titles_info[n].text.strip(' ').replace('\n', '~'))
data = dict(zip(titles, infos))


driver.quit()
