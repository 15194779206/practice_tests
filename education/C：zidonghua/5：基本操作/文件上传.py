#
from selenium import webdriver
import time

brower=webdriver.Firefox()
brower.get(r"file:///C:/Users/liunan/Desktop/test.html")
brower.find_element_by_name('file').send_keys(r'C:\Users\liunan\Desktop\artlogo\1.jpg')