#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_200130_PageObject.PageLocators.index_page_locator import IndexPageLocator as loc

class IndexPage:
    """首页--业务操作封装"""

    def __init__(self,driver):
        self.driver = driver

    def approve_management_page(self):
        """跳转到审批管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.approve_management))
        self.driver.find_element(*loc.approve_management).click()

    def project_management_page(self):
        """跳转到项目管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.project_management))
        self.driver.find_element(*loc.project_management).click()

    def field_management_page(self):
        """跳转到案场管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.field_management))
        self.driver.find_element(*loc.field_management).click()

    def finance_management_page(self):
        """跳转到财务管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.finance_management))
        self.driver.find_element(*loc.finance_management).click()

    def agency_management_page(self):
        """跳转到中介管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.agency_management))
        self.driver.find_element(*loc.agency_management).click()

    def quality_management_page(self):
        """跳转到品控管理页面"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.quality_management))
        self.driver.find_element(*loc.quality_management).click()

    def logout_system(self):
        """退出系统"""
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.logout_button))
        self.driver.find_element(*loc.logout_button).click()

    def isExist_logout_ele(self):
        """判断“退出”按钮是否存在"""
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.logout_button))
            return True
        except:
            return False