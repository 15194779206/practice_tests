from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public import Login

dr=webdriver.Firefox()
dr.get('https://www.126.com/')

#数据化驱动
usern='user'
passw='1234'

l=Login(dr)
l.login(usern,passw)
