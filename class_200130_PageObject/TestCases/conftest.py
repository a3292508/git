#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
import warnings
from selenium import webdriver
from class_200130_PageObject.PageObjects.login_page import LoginPage

driver = None

@pytest.fixture(scope="class")
def access_web():
    #前置操作
    global driver
    driver = webdriver.Chrome()
    driver.get('http://hoss.haowu.com/hoss-web/hoss-v2/app/account/login.html')
    driver.maximize_window()
    Login = LoginPage(driver)
    yield (driver,Login)        #分割线，后面接返回值
    #后置操作
    driver.quit()

@pytest.fixture()
def refresh_page():
    global driver
    warnings.simplefilter('ignore', ResourceWarning)
    #前置操作
    yield
    #后置操作
    driver.refresh()