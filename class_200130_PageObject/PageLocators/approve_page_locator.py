#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By

class ApprovePageLocator:
    """审批管理页--页面元素封装"""

    #费用申请单
    fee_apply = (By.XPATH,'//a[@processkey="FYSQ"]')