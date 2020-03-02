#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
import allure
from class_200130_PageObject.PageObjects.index_page import IndexPage
from class_200130_PageObject.TestDatas.login_data import success_data,error_data

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    @pytest.mark.parametrize("data",error_data)
    @pytest.mark.smoke
    def test_phone_form_error(self,access_web,data):
        """账号或密码错误"""
        access_web[1].login(data['username'],data['password'])
        assert access_web[1].isExist_user() == data['check']

    @pytest.mark.smoke
    def test_login_success(self, access_web):  # fixture的函数名称作为用例参数，用来接收fixture的返回值，可以放多个
        """登录成功"""
        access_web[1].login(success_data['username'], success_data['password'])
        assert IndexPage(access_web[0]).isExist_logout_ele()