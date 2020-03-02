#!usr/bin/env python
#-*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

#获取应用包名和入口activity：aapt命令
#在aapt目录下：C:\Users\17486\AppData\Local\adt-bundle-windows\sdk\build-tools\android-4.4W
#执行aapt dump badging apk应用名（加上路径）

desired_caps = {}
desired_caps["platformName"] = "Android"                #平台类型
desired_caps["platformVersion"] = "5.1"                 #平台版本号
desired_caps["deviceName"] = "Android Emulator"         #设备名称
desired_caps["appPackage"] = "cn.haowu.agent"           #app包名
# desired_caps["appActivity"] = "cn.haowu.agent.module.welcomeOrGuide.WelcomeActivity"            #app入口（默认页面）
desired_caps["appActivity"] = "cn.haowu.agent.module.login.LoginActivity"
desired_caps["noReset"] = True                          #重置与否

#连接appium server。前提：appium desktop要启动,有监听端口
#将desired_caps(服务器参数)发送过去
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#输入账号
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"cn.haowu.agent:id/et_name")))
driver.find_element_by_id("cn.haowu.agent:id/et_name").send_keys("16602159899")
#输入密码
driver.find_element_by_id("cn.haowu.agent:id/et_passwd").send_keys("111111")
#点击登录
driver.find_element_by_id("cn.haowu.agent:id/btv_user_name_login").click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"cn.haowu.agent:id/img_head")))
#滑动到客户列表
size = driver.get_window_size()
start_x = size["width"] * 0.8
start_y = size["height"] *0.5
end_x = size["width"] * 0.1
end_y = size["height"] *0.5
driver.swipe(start_x,start_y,end_x,end_y,200)

