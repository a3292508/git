#!usr/bin/env python
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By

class LoginPageLocator:
    """登录页--页面元素封装"""

    #用户名输入框
    username_ele = (By.XPATH,'//input[@id="username"]')
    #密码输入框
    password_ele = (By.XPATH,'//input[@id="password"]')
    #登录按钮
    submit_ele = (By.XPATH,'//input[@class="submit hand"]')
    #忘记密码
    forget_password_ele = (By.XPATH,'//a[@id="forgetPwd"]')
    #错误提示
    error_meg_ele = (By.XPATH,'//div[@class="error-message"]')