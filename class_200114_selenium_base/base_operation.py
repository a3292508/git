#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

from selenium import webdriver
#指定浏览器驱动
driver = webdriver.Chrome()
#打开网页
driver.get('http://www.baidu.com')
#页面最大化
driver.maximize_window()
#打开另一网页
driver.get('https://note.youdao.com/')
#回退到旧网页
driver.back()
#再次进入到新网页
driver.forward()
#刷新网页
driver.refresh()
#关闭当前网页
# driver.close()
#打印当前页面句柄
print(driver.current_window_handle)
#打印当前页面url
print(driver.current_url)
#打印当前页面标题
print(driver.title)
#关闭浏览器和驱动服务
driver.quit()