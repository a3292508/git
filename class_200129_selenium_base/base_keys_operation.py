#!usr/bin/env python
#-*- coding:utf-8 -*-

#键盘操作

#需要借助send_keys()来模拟操作
#常用组合键：
#send_keys(Keys.CONTROL,'a')        全选
#send_keys(Keys.CONTROL,'c')        复制
#send_keys(Keys.CONTROL,'x')        剪切
#send_keys(Keys.CONTROL,'v')        粘贴
#常用非组合键：
# Keys.ENTER           回车
# Keys.BACK_SPACE      删除
# Keys.SPACE           空格
# Keys.TAB             制表
# Keys.ESCAPE          回退
# Keys.F5              刷新

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

driver.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班")
driver.find_element_by_xpath('//input[@id="su"]').send_keys(Keys.ENTER)
