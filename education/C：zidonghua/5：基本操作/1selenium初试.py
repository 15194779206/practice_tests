from selenium import webdriver
import time


brower=webdriver.Firefox()
time.sleep(2)
brower.get(r'file:///C:/Users/liunan/Desktop/test.html')
