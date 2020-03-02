#!usr/bin/env python
#-*- coding:utf-8 -*-

from web_auto.PageLocators.index_page_locator import IndexPageLocator as loc
from web_auto.Common.base_page import BasePage

class IndexPage(BasePage):
    """首页--业务操作封装"""

    def approve_management_page(self):
        """跳转到审批管理页面"""
        self.wait_element_visible(loc.approve_management)
        self.click_element(loc.approve_management)

    def project_management_page(self):
        """跳转到项目管理页面"""
        self.wait_element_visible(loc.project_management)
        self.click_element(loc.project_management)

    def field_management_page(self):
        """跳转到案场管理页面"""
        self.wait_element_visible(loc.field_management)
        self.click_element(loc.field_management)

    def finance_management_page(self):
        """跳转到财务管理页面"""
        self.wait_element_visible(loc.finance_management)
        self.click_element(loc.finance_management)

    def agency_management_page(self):
        """跳转到中介管理页面"""
        self.wait_element_visible(loc.agency_management)
        self.click_element(loc.agency_management)

    def quality_management_page(self):
        """跳转到品控管理页面"""
        self.wait_element_visible(loc.quality_management)
        self.click_element(loc.quality_management)

    def logout_system(self):
        """退出系统"""
        self.wait_element_visible(loc.logout_button)
        self.click_element(loc.logout_button)

    def isExist_logout_ele(self):
        """判断'退出'按钮是否存在"""
        try:
            self.wait_element_visible(loc.logout_button)
            return True
        except:
            return False