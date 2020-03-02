#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By

class IndexPageLocator:
    """首页--页面元素封装"""

    #工作台
    work_bench = (By.XPATH,'//a[text()="工作台"]')
    #审批管理
    approve_management = (By.XPATH,'//a[text()="审批管理"]')
    #项目管理
    project_management = (By.XPATH,'//a[text()="项目管理"]')
    #案场管理
    field_management = (By.XPATH, '//a[text()="案场管理"]')
    #财务管理
    finance_management = (By.XPATH, '//a[text()="财务管理"]')
    #品控管理
    quality_management = (By.XPATH, '//a[text()="品控管理"]')
    #运营管理
    operation_management = (By.XPATH, '//a[text()="运营管理"]')
    #中介管理
    agency_management = (By.XPATH, '//a[text()="中介管理"]')
    #预拓展管理
    pre_development_management = (By.XPATH, '//a[text()="预拓展管理"]')
    #退出按钮
    logout_button = (By.XPATH, '//a[@id="logout"]')