#!usr/bin/env python
#-*- coding:utf-8 -*-

from class_200225_appium_auto.Common.base_page import BasePage
from class_200225_appium_auto.PageLocators.login_page_locator import LoginPageLocator as loc

class LoginPage(BasePage):
    """登录页---业务操作封装"""

    def login(self,username,password):
        """登录操作"""
        self.wait_element_visible(loc.username_ele)
        self.input_text(loc.username_ele,username)
        self.input_text(loc.password_ele,password)
        self.click_element(loc.submit_ele)

    def code_login(self):
        """跳转使用验证码登录页面"""
        self.wait_element_visible(loc.code_login_ele)
        self.click_element(loc.code_login_ele)

    def register_account(self):
        """跳转注册账号页面"""
        self.wait_element_visible(loc.register_ele)
        self.click_element(loc.register_ele)

    def forget_password(self):
        """跳转忘记密码页面"""
        self.wait_element_visible(loc.forget_password_ele)
        self.click_element(loc.forget_password_ele)

    def get_error_message(self):
        """获取错误信息提示"""
        self.wait_element_present()
        return self.driver