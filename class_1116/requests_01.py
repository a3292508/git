#!usr/bin/env python
#-*- coding:utf-8 -*-

# requests库
import requests

#get请求
# url = 'https://www.baidu.com'
# res = requests.get(url,params='requests')     #响应结果的消息实体
# print(res)
# print('响应头：',res.headers)
# print('响应状态码：',res.status_code)
# print('响应体：',res.text)

#post请求
url = 'https://www.juhe.cn/login/login'
data = {'username':'16602159899','password':'zyj16602159899'}
headers = {'User-Agent':'Mozilla/5.0'}
res = requests.post(url,data=data,headers=headers,verify=False)      #响应结果的消息实体
print(res.json())
# print('响应头：',res.headers)
# print('响应状态码：',res.status_code)
# print('响应体1：',res.text,type(res.text))
# print('响应体2：',res.json(),type(res.json()))      #推荐使用第二种方式，方便取值
# print('cookies:',res.cookies)       #类字典形式
# print('acw-tc:',res.cookies['acw_tc'])
# print('代理user-agent:',res.request.headers)      #请求头