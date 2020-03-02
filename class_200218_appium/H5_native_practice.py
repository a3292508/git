#!usr/bin/env python
#-*- coding:utf-8 -*-

from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps["platformName"] = "Android"                #平台类型
desired_caps["platformVersion"] = "5.1"                 #平台版本号
desired_caps["deviceName"] = "Android Emulator"         #设备名称
desired_caps["appPackage"] = "cn.haowu.agent"           #app包名
# desired_caps["appActivity"] = "cn.haowu.agent.module.welcomeOrGuide.WelcomeActivity"            #app入口（默认页面）
desired_caps["appActivity"] = "cn.haowu.agent.module.login.LoginActivity"
# desired_caps["noReset"] = True                          #重置与否

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#输入账号
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"cn.haowu.agent:id/et_name")))
driver.find_element_by_id("cn.haowu.agent:id/et_name").send_keys("16602159899")
#输入密码
driver.find_element_by_id("cn.haowu.agent:id/et_passwd").send_keys("111111")
#点击登录
driver.find_element_by_id("cn.haowu.agent:id/btv_user_name_login").click()

#点击“好屋精选”
loc = 'new UiSelector().text("好屋精选")'
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,loc)))
driver.find_element_by_android_uiautomator(loc).click()
#等待WebView元素出现---html页面
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME,"android.webkit.WebView")))
sleep(2)

# 前提：代码可以识别到webview；需要开启app的webview debug
# 1.列出所有的contexts
cons = driver.contexts
print(cons)
current_con = driver.current_context
print(current_con)
#2.切换至webview。要确保chromedriver的版本与webView的版本匹配，也要放置在对应的位置。
driver.switch_to.context(cons[1])
#3.切换之后，当前的操作对象变为html页面
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.XPATH,'//li[@cid="22"]/a')))
driver.find_element_by_xpath('//li[@cid="22"]/a').click()