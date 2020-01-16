#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#指定浏览器驱动
driver = webdriver.Chrome()
#打开网页
driver.get('http://www.baidu.com')
#页面最大化
driver.maximize_window()

driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_login']").click()

#1.强制等待
# sleep(5)
#2.隐式等待:整个driver的会话周期内，设置一次即可，全局可用
# driver.implicitly_wait(10)
#3.显式等待:
# 明确等待某个条件满足后，再去执行下一步操作。如果超过设置的最长时间，会抛出TimeoutException

id = 'TANGRAM__PSP_10__footerULoginBtn'
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID,id))
)
driver.find_element_by_xpath('//p[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

#用法:
#1.先确定元素的定位表达式
#2.调用WebdriverWait类设置等待总时长，轮询周期。并调用until、until_not方法。即WebDriverWait(driver,等待总时长，轮询周期).until(判断条件)
#3.使用expected_conditions对应的方法来生成判断条件。即EC.类名(定位方式，定位表达式)

# expected_conditions对应的方法：
# title_is(object)：检查页面标题是否为预期的标题，必须完全匹配，如果标题匹配，则返回True，否则返回False。

# title_contains(object)：检查页面标题是否包含区分大小写的字符串。当标题匹配时返回True，否则返回False。

# presence_of_element_located(object)：检查某个元素是否存在于页面，不论元素是否可见。当某个元素存在则返回True，否则返回False。

# presence_of_all_elements_located(object)：检查是否至少有一个满足条件的元素存在于页面。存在时返回True，否则返回False。

# visibility_of_element_located(object)：检查某个元素是否存在于页面和可见。可见性意味着不仅显示元素但高度和宽度也大于0。当某个元素存在则返回True，否则返回False。

# visibility_of_all_elements_located(object)：检查所有满足条件的元素是否存在于页面和可见。可见性意味着不仅显示元素但高度和宽度也大于0。当所有元素都存在时则返回True，否则返回False。

# url_to_be：检查当前的url是否是所需的url，必须完全匹配。如果匹配时则返回True，否则返回False。

# url_contains(object)：检查当前URL是否包含区分大小写的子字符串。如果匹配时则返回True，否则返回False。

# url_changes(object)：检查当前的url是否是所需的url，不能完全匹配。当不能匹配时则返回True，否则返回False。

# text_to_be_present_in_element(object)：检查给指定文本是否存在于指定元素。如果存在指定文本则返回True，否则返回False。

# text_to_be_present_in_element_value(object)：检查给指定文本是否存在于指定元素的属性值。如果存在指定文本则返回True，否则返回False。

