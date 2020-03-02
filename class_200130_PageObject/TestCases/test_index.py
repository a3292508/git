#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from time import sleep
from selenium import webdriver
from class_200130_PageObject.PageObjects.index_page import IndexPage
from class_200130_PageObject.PageObjects.login_page import LoginPage
from class_200130_PageObject.TestDatas.login_data import success_data

class TestIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://hoss.haowu.com/hoss-web/hoss-v2/app/account/login.html')
        cls.driver.maximize_window()
        cls.Index = IndexPage(cls.driver)
        #登录系统
        LoginPage(cls.driver).login(success_data['username'], success_data['password'])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass
    def tearDown(self):
        sleep(1)

    def test_0_skipTo_approve_management_page(self):
        """跳转到审批管理页面"""
        self.Index.approve_management_page()

    def test_0_skipTo_project_management_page(self):
        """跳转到项目管理页面"""
        self.Index.project_management_page()

    def test_0_skipTo_field_management_page(self):
        """跳转到案场管理页面"""
        self.Index.field_management_page()

    def test_0_skipTo_finance_management_page(self):
        """跳转到财务管理页面"""
        self.Index.finance_management_page()

    def test_0_skipTo_quality_management_page(self):
        """跳转到品控管理页面"""
        self.Index.quality_management_page()

    def test_0_skipTo_agency_management_page(self):
        """跳转到中介管理页面"""
        self.Index.agency_management_page()

    def test_1_logout_system(self):
        """退出系统"""
        self.Index.logout_system()

if __name__ == '__main__':
    unittest.main()