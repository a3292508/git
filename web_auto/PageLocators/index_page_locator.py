#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By

class IndexPageLocator:
    """首页--页面元素封装"""

    # 工作台按钮
    work_bench = (By.XPATH, '//a[text()="工作台"]')
    # 审批管理按钮
    approve_management = (By.XPATH, '//a[text()="审批管理"]')
    # 项目管理按钮
    project_management = (By.XPATH, '//a[text()="项目管理"]')
    # 案场管理按钮
    field_management = (By.XPATH, '//a[text()="案场管理"]')
    # 财务管理按钮
    finance_management = (By.XPATH, '//a[text()="财务管理"]')
    # 品控管理按钮
    quality_management = (By.XPATH, '//a[text()="品控管理"]')
    # 运营管理按钮
    operation_management = (By.XPATH, '//a[text()="运营管理"]')
    # 中介管理按钮
    agency_management = (By.XPATH, '//a[text()="中介管理"]')
    # 预拓展管理按钮
    pre_development_management = (By.XPATH, '//a[text()="预拓展管理"]')
    # 退出按钮
    logout_button = (By.XPATH, '//a[@id="logout"]')