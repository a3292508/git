#!usr/bin/env python
#-*- coding:utf-8 -*-

from class_200225_appium_auto.Common.base_page import BasePage

class IndexPage(BasePage):
    """首页--业务操作封装"""
    def get_login_status(self):
        """获取当前登录状态，已登录为True，未登录为False"""
        try:
            "等待5秒，找登录按钮"
            return False
        except:
            return True