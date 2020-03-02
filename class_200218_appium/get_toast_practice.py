#!usr/bin/env python
#-*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"         #自动化测试引擎
desired_caps["platformName"] = "Android"                #平台类型
desired_caps["platformVersion"] = "5.1"                 #平台版本号
desired_caps["deviceName"] = "Android Emulator"         #设备名称
desired_caps["appPackage"] = "cn.haowu.agent"           #app包名
# desired_caps["appActivity"] = "cn.haowu.agent.module.welcomeOrGuide.WelcomeActivity"            #app入口（默认页面）
desired_caps["appActivity"] = "cn.haowu.agent.module.login.LoginActivity"
# desired_caps["noReset"] = True                          #重置与否

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#输入账号
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"cn.haowu.agent:id/et_name")))
# driver.find_element_by_id("cn.haowu.agent:id/et_name").send_keys("16602159899")
#输入密码
# driver.find_element_by_id("cn.haowu.agent:id/et_passwd").send_keys("111111")
#点击登录
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"cn.haowu.agent:id/btv_user_name_login")))
driver.find_element_by_id("cn.haowu.agent:id/btv_user_name_login").click()

#1.xpath表达式---文本匹配
loc = (MobileBy.XPATH,'//*[contains(text,"{0}")]'.format("手机号码不能为空"))
#2.等待的方法要用prensence_of_element_located
try:
    WebDriverWait(driver,20,0.01).until(EC.presence_of_element_located(loc))
    print(driver.find_element_by_xpath('//*[contains(text,"手机号码不能为空")]').text)
except:
    print("没有找到toast！")
