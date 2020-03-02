#!usr/bin/env python
#-*- coding:utf-8 -*-

#鼠标操作
#由selenium的ActionChains类来完成模拟鼠标操作
#主要操作流程：1.存储鼠标操作；2.perform()来执行鼠标操作

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

#一：鼠标悬停操作

#1.先找到鼠标要操作的元素
setting_ele = driver.find_element_by_xpath('//div[@id="u1"]/a[text()="设置"]')
#2.实例化ActionChains类
# action = ActionChains(driver)
#3.将鼠标操作添加到actions列表中
# action.move_to_element(setting)
#4.调用perform()函数来执行鼠标操作
# action.perform()

#可将2/3/4步放在一起操作
ActionChains(driver).move_to_element(setting_ele).perform()
#下拉列表处理方式一：
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]'))
)
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()
