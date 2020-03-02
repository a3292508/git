#!usr/bin/env python
#-*- coding:utf-8 -*-

#登录功能测试数据

#登录成功
success_data = {"username":"16602159899","password":"Zyj888888"}

#异常数据
error_data = [
    {"username":"1660215989","password":"Zyj888888","check":"用户不存在!"},
    # {"username":"166021598999","password":"Zyj888888","check":"用户不存在!"},
    # {"username":"12345678999","password":"Zyj888888","check":"用户不存在!"},
    {"username":"","password":"Zyj888888","check":"请输入您的账号"},
    {"username":"16602159899","password":"111111","check":"用户名密码不匹配!"},
    # {"username":"16602159899","password":"","check":"密码不能小于六位"}
]