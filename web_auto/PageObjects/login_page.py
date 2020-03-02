#!usr/bin/env python
#-*- coding:utf-8 -*-

from web_auto.PageLocators.login_page_locator import LoginPageLocator as loc
from web_auto.Common.base_page import BasePage

class LoginPage(BasePage):
    """登录页--业务操作封装"""

    def login(self,username,password):
        """登录操作"""
        self.wait_element_visible(loc.username_ele)
        self.input_text(loc.username_ele,username)
        self.input_text(loc.password_ele,password)
        self.click_element(loc.submit_ele)

    def forget_password(self):
        """跳转忘记密码页面"""
        self.wait_element_visible(loc.forget_password_ele)
        self.click_element(loc.forget_password_ele)

    def error_message(self):
        """错误信息提示"""
        self.wait_element_visible(loc.error_meg_ele)
        return self.get_element_text(loc.error_meg_ele)