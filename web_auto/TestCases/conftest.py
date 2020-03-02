#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from selenium import webdriver
from web_auto.PageObjects.login_page import LoginPage
from web_auto.TestDatas.common_data import prd_url

driver = None

@pytest.fixture(scope="class")
def access_web():
    """网页打开及关闭"""
    global driver
    driver = webdriver.Chrome()         #选择浏览器驱动
    driver.get(prd_url)                 #打开网页
    driver.maximize_window()            #窗口最大化
    Login = LoginPage(driver)
    yield (driver,Login)
    driver.quit()

@pytest.fixture(scope="function")
def refresh_page():
    """刷新页面"""
    global driver
    yield
    driver.refresh()
