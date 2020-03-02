#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_200130_PageObject.PageLocators.login_page_locator import LoginPageLocator as loc
from class_200130_PageObject.Common.base_page import BasePage

class LoginPage(BasePage):
    """登录页--业务操作封装"""

    def login(self,username,password):
        """登录操作"""
        doc = '登录页面_登录操作'
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.username_ele))
        # self.driver.find_element(*loc.username_ele).send_keys(username)
        # self.driver.find_element(*loc.password_ele).send_keys(password)
        # self.driver.find_element(*loc.submit_ele).click()
        self.wait_element_visible(loc.username_ele,doc)
        self.input_text(loc.username_ele,username,doc)
        self.input_text(loc.password_ele,password,doc)
        self.click_element(loc.submit_ele,doc)

    def forget_password(self):
        """忘记密码"""
        doc = '登录页面_忘记密码'
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.forget_password_ele))
        # self.driver.find_element(*loc.forget_password_ele).click()
        self.wait_element_visible(loc.forget_password_ele,doc)
        self.click_element(loc.forget_password_ele,doc)

    def isExist_user(self):
        """错误提示"""
        doc = '登录页面_错误提示'
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.error_meg_ele))
        # return self.driver.find_element(*loc.error_meg_ele).text
        self.wait_element_visible(loc.error_meg_ele,doc)
        return self.get_element_text(loc.error_meg_ele,doc)
