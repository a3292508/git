#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
class HttpRequest:
    """利用requests封装get请求和post请求"""
    def http_request(self,method,url,data,cookie=None):
        """
        method:请求方式，支持get/post
        url:请求的地址
        data:传递的参数，非必填，字典的格式传递
        cookie:请求时传递的cookie值
        """
        #响应结果的消息实体
        if method.lower() == 'get':
            res = requests.get(url,data,cookies=cookie)
        elif method.lower() == 'post':
            res = requests.post(url,data,cookies=cookie)
        #返回一个消息实体
        return res

if __name__ == '__main__':
    HttpRequest().http_request()