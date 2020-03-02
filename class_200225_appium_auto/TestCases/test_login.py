#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from class_200225_appium_auto.PageObjects.login_page import LoginPage

class TestLogin:
    """登录页测试用例"""

    @pytest.mark.usefixtures("startApp")
    def test_login_success(self,startApp):
        """登录成功"""
        startApp[1].login("16602159899","111111")
        assert 1==1