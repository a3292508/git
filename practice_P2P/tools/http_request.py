#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests

class HttpRequest:

    # @staticmethod     #可以设置成静态函数
    def http_request(self,url,data,http_method,cookie=None):
        try:
            if http_method.upper()=='GET':
                res = requests.get(url,data,cookies=cookie)
            elif http_method.upper()=='POST':
                res = requests.post(url,data,cookies=cookie)
            else:
                print('输入的请求方式错误！')
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res

if __name__ == '__main__':

    # 注册
    register_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    register_data = {"mobilephone":"15096099000","pwd":"123456","regname":"小小"}

    # 登录
    login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    login_data = {"mobilephone":"15096099000","pwd":"123456"}

    # 充值
    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    recharge_data = {"mobilephone":"15096099000","amount":"1000"}

    login_res = HttpRequest().http_request(login_url,login_data,'get')
    recharge_res = HttpRequest().http_request(recharge_url,recharge_data,'post',login_res.cookies)
    print("充值的结果是：{0}".format(recharge_res.json()))