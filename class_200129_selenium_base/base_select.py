#!usr/bin/env python
#-*- coding:utf-8 -*-

# Select类：下拉框操作
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

setting_ele = driver.find_element_by_xpath('//div[@id="u1"]/a[text()="设置"]')
ActionChains(driver).move_to_element(setting_ele).perform()
#下拉列表处理方式一：
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]'))
)
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
#找到select元素
select_ele = driver.find_element_by_xpath('//select[@name="ft"]')
#方式一：通过下标选择下拉列表值，从0开始
Select(select_ele).select_by_index(3)
sleep(1)
#方式二：通过value值选择下拉列表值
Select(select_ele).select_by_value('all')
sleep(1)
#方式三：通过文本内容来选择下拉列表值
Select(select_ele).select_by_visible_text('Adobe Acrobat PDF (.pdf)')