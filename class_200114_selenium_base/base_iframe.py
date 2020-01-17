#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#切换iframe的用法

driver = webdriver.Chrome()
driver.get('https://ke.qq.com/')
driver.maximize_window()

#方式一：点击切换iframe--进入另一个html
#用法:
#driver.switch_to.frame('frame_name')       iframe的name
#driver.switch_to.frame(1)                  iframe的序号
#driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])          先定位到元素的位置，然后跳转
driver.switch_to.frame('login_frame_qq')
driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="login_frame_qq"]'))

# 方式二：使用显式等待,不需要再次跳转
WebDriverWait(driver,20).until(
    EC.frame_to_be_available_and_switch_to_it('login_frame_qq')
)
sleep(0.5)

#从iframe中回到默认的页面中
driver.switch_to.default_content()
#跳转到上级iframe中(有多级iframe嵌套时可使用)
driver.switch_to.parent_frame()