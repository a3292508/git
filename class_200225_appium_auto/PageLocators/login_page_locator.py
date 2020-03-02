#!usr/bin/env python
#-*- coding:utf-8 -*-

from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocator:
    """登录页--页面元素封装"""

    #账号输入框
    username_ele = (MobileBy.ID,"cn.haowu.agent:id/et_name")
    #密码输入框
    password_ele = (MobileBy.ID, "cn.haowu.agent:id/et_passwd")
    #登录按钮
    submit_ele = (MobileBy.ID, "cn.haowu.agent:id/btv_user_name_login")
    #使用验证码登录
    code_login_ele = (MobileBy.ID,"cn.haowu.agent:id/tv_verification_code_login")
    #注册账号
    register_ele = (MobileBy.ID,"cn.haowu.agent:id/tv_register")
    #忘记密码
    forget_password_ele = (MobileBy.ID, "cn.haowu.agent:id/tv_forget_passwd")