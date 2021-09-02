from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Action(object):
    """
    这个类主要是完成所有页面的一些公共方法的封装
    """
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 定义open方法
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 重写元素定位的方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            return ("通过%s方法，未找到元素%s"%loc)

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            return "通过%s方法，未找到元素%s" %loc

    def ActionChains(self, *loc):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc)).perform()

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.execute_script('arguments[0].scrollIntoView()', src)

    # 重写send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            self.obj = self.find_element(*loc)
            if click_first:
                self.obj.click()
            if clear_first:
                self.obj.clear()
            self.obj.send_keys(value)
        except AttributeError:
            print(self.obj)
