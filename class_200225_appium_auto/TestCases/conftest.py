#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from appium import webdriver
from time import sleep
from class_200225_appium_auto.Common.base_page import BasePage
from class_200225_appium_auto.PageObjects.login_page import LoginPage
from class_200225_appium_auto.Common.project_path import caps_dir

@pytest.fixture()
def startApp():
    """启动app"""
    "要不要判断欢迎页面是否存在？"
    "要不要判断当前用户是否已登录？（可以走接口）"
    "如果已登录，要先退出（可以走接口）"
    desired_caps = {}
    desired_caps["platformName"] = "Android"  # 平台类型
    desired_caps["platformVersion"] = "5.1"  # 平台版本号
    desired_caps["deviceName"] = "Android Emulator"  # 设备名称
    desired_caps["appPackage"] = "cn.haowu.agent"  # app包名
    desired_caps["appActivity"] = "cn.haowu.agent.module.login.LoginActivity"
    desired_caps["noReset"] = True  # 重置与否
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    Login = LoginPage(driver)
    yield (driver,Login)


def handle_welcome(driver):
    """处理欢迎页面"""
    current_Act = driver.current_activity
    if current_Act.find("LoginActivity") == -1:
        #左划三次，点击立即体验，跳转到登录页
        size = BasePage(driver).get_size()
        for i in range(3):
            BasePage(driver).swipe_left(size)
            sleep(1)
        BasePage(driver).click_element("")

def baseDriver():
    """将默认的配置数据读取出来"""





