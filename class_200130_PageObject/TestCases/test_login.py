#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
import unittest
from class_200130_PageObject.PageObjects.login_page import LoginPage
from class_200130_PageObject.PageObjects.index_page import IndexPage
from class_200130_PageObject.TestDatas.login_data import success_data,error_data
from ddt import ddt,data
import warnings

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://hoss.haowu.com/hoss-web/hoss-v2/app/account/login.html')
        cls.driver.maximize_window()
        cls.Login = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self):
        self.driver.refresh()

    def test_1login_success(self):
        """登录成功"""
        self.Login.login(success_data['username'],success_data['password'])
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    @data(*error_data)
    def test_0phone_form_error(self,data):
        """账号或密码错误"""
        self.Login.login(data['username'],data['password'])
        self.assertEqual(self.Login.isExist_user(),data['check'])

if __name__ == '__main__':
    unittest.main()