#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
from web_auto.TestDatas.login_data import success_data,error_data
from web_auto.PageObjects.index_page import IndexPage

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    @pytest.mark.parametrize('data',error_data)
    def test_login_failure(self,access_web,data):
        """登录失败"""
        access_web[1].login(data["username"], data["password"])
        assert access_web[1].error_message() == data["check"]

    @pytest.mark.smoke
    def test_login_success(self,access_web):
        """登录成功"""
        access_web[1].login(success_data["username"],success_data["password"])
        assert IndexPage(access_web[0]).isExist_logout_ele()