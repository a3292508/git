#!usr/bin/env python
#-*- coding:utf-8 -*-

# 类的封装
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
    url = 'http://api.juheapi.com/japi/toh'
    data ={'key':'9f6742f2a66e61bf8f6c403b909f01f9','v':'1.0','month':'11','day':'17'}
    res = HttpRequest().http_request('post',url,data)
    print(res.json())

    url = 'http://v.juhe.cn/chengyu/query'
    data = {'key': '0042c0aada14f6c87abbaa668fbb1dfc', 'v': '1.0', 'word': '朝三暮四'}
    res = HttpRequest().http_request('get', url, data)
    print(res.json())