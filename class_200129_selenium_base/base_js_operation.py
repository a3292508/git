#!usr/bin/env python
#-*- coding:utf-8 -*-

#常见JS操作用法
#执行JS语法操作：driver.execute_script(JS语句)
#一般可以用来处理滚动条/日期框

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

driver.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班")
driver.find_element_by_xpath('//input[@id="su"]').send_keys(Keys.ENTER)
sleep(1)

#滚动条处理

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="Lemfix"]')))
ele = driver.find_element_by_xpath('//a[text()="Lemfix"]')
#移动到元素element对象的"底部"与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollIntoView(false);",ele)
#移动到元素element对象的"顶端"与当前窗口的“顶部”对齐
sleep(1)
ele = driver.find_element_by_xpath('//a[text()="吧_百度贴吧"]')
driver.execute_script("arguments[0].scrollIntoView();",ele)
#移动到页面底部
sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#移动到页面顶部
sleep(1)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

#js语句
js = 'var ele = document.getElementById("train_date");ele.readOnly = false;ele.value = "2020-02-10";'
driver.execute_script(js)