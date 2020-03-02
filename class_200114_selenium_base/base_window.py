#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#切换窗口的用法
#1.获取窗口的总数以及句柄，新打开的窗口位于句柄列表中最后一个
#2.执行切换窗口操作

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.find_element_by_xpath('//input[@id="kw"]').send_keys('柠檬班')
driver.find_element_by_xpath('//input[@id="su"]').click()
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"吧_百度贴吧")]'))
)

# 方法一：（打开新页面之后再获取句柄）
# driver.find_element_by_xpath('//a[contains(text(),"吧_百度贴吧")]').click()
# #获取所有页面的句柄（列表）
# handles = driver.window_handles
# print(handles)
#
# #获取当前页面的句柄
# current_window = driver.current_window_handle
# print(current_window)
#
# #切换窗口
# driver.switch_to.window(handles[-1])
# WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.ID,'j_head_focus_btn'))
# )
# driver.find_element_by_xpath('//a[@id="j_head_focus_btn"]').click()

# 方法二：使用显式等待（打开新页面之前获取句柄）
handles = driver.window_handles
print(handles)
#打开新页面
driver.find_element_by_xpath('//a[contains(text(),"吧_百度贴吧")]').click()
#通过句柄数量的变化，判断是否打开新页面
WebDriverWait(driver,10).until(
    EC.new_window_is_opened(handles)
)
#需要重新获取一次句柄列表
handles = driver.window_handles
driver.switch_to.window(handles[-1])
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID,'j_head_focus_btn'))
)
driver.find_element_by_xpath('//a[@id="j_head_focus_btn"]').click()

#返回之前窗口
# driver.switch_to.window(handles[0])

