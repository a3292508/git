#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_200130_PageObject.PageLocators.approve_page_locator import ApprovePageLocator as loc

class ApprovePage:
    """审批管理页--业务操作封装"""