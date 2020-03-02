#!usr/bin/env python
#-*- coding:utf-8 -*-

# alert弹出框的切换

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('C:\\Users\\17486\\PycharmProjects\\python_11\\class_200114_selenium_base\\base_practice_HTML.html')

#使用显式等待判断是否有弹框，然后将操作跳转到弹框中
WebDriverWait(driver,10).until(
    EC.alert_is_present()
)
alert = driver.switch_to.alert      #跳转到弹出框
print(alert.text)                   #打印弹框内容
alert.accept()                      #同意并关闭弹框
# alert.dismiss()                     #取消并关闭弹框
# alert.send_keys('eee')              #往输入框中输入文本
