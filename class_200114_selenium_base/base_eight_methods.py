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

# 方法一：使用id定位
driver.find_element_by_id('kw')
#方法二：使用name定位
driver.find_element_by_name('wd')
#方法三：使用class_name定位
driver.find_element_by_class_name('s_ipt')
#方法四：使用tag_name定位
driver.find_element_by_tag_name('input')
#方法五：使用文本内容定位
driver.find_element_by_link_text('新闻')
#方法六：使用部分文本内容模糊定位
driver.find_element_by_partial_link_text('更多')
#方法七：使用xpath定位：
driver.find_element_by_xpath('//input[@id="kw"]')                   #一般用法
driver.find_element_by_xpath('//input[@id="kw" and @name="wd"]')    #使用逻辑运算符and或者or
driver.find_element_by_xpath('//div[@id="ul"]/span/a')              #使用层级定位，/和//都可以
driver.find_element_by_xpath('//input[text()="更多产品"]')           #使用text()
driver.find_element_by_xpath('//input[contains(@class,"s_ipt")]')    #使用contains()方法
driver.find_element_by_xpath('//input[contains(text(),"更多产品")]')    #使用contains()方法
driver.find_element_by_xpath('//span[text()="python10专用"]/ancestor::a/following-sibling::div//a')       #使用轴定位，前面必须用/（单斜杠）

#轴定位方法
# ancestor:祖先节点 包括父节点
# parent:父节点
# preceding:当前元素节点标签之前的所有节点
# preceding-sibling:当前元素节点标签之前的所有兄弟节点
# following:当前元素节点标签之后的所有节点
# following-sibling:当前元素节点标签之后的所有兄弟节点

# 使用语法：/轴名称::节点名称[@属性=值]
# 例子：//span[text()='python10专用']/ancestor::a/following-sibling::div//a      通过span去定位div下的a标签
#应用场景：页面显示为一个表格样式的数据列，需要通过组合来定位元素