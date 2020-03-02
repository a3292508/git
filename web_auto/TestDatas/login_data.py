#!usr/bin/env python
#-*- coding:utf-8 -*-

"""登录页--数据"""

#正常数据
success_data = {"username": "16602159899", "password": "Zyj888888"}

#异常数据
error_data = [
    {"username": "1660215989", "password": "Zyj888888", "check": "用户不存在!"},         #账号错误
    # {"username":"12345678999","password":"Zyj888888","check":"用户不存在!"},             #账号错误
    {"username": "", "password": "Zyj888888", "check": "请输入您的账号"},                #账号为空
    {"username": "16602159899", "password": "111111", "check": "用户名密码不匹配!"},     #密码错误
    # {"username":"16602159899","password":"","check":"密码不能小于六位"}                  #密码为空
]