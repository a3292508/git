#!usr/bin/env python
#-*- coding:utf-8 -*-

#正则表达式：用一个规则匹配你想要的信息
#两个重要的点：元字符/限定符
#元字符：
# . 任意单个字符
# \d 任意单个数字
# [0-9] 等价0-9
# [a-zA-Z] 等价所有的大小写字母

#限定符：
#+ 匹配至少大于1次
#? 匹配0次或1次
#* 匹配0次或多次 贪婪匹配
#{n,}/{n,m}/{n} 匹配限定次数  {n,}指大于n次，{n}指固定的n次

import re
from practice_P2P.tools.get_data import GetData
# s = 'www.lemfix.com'    #目标字符串
# res = re.match('(w)(ww)',s)     #全匹配，头部匹配
# print(res)
# print(res.group())      #分组查看匹配结果，括号内可输入数字，根据正则表达式里的括号分组！group()和group(0)代表拿到的所有字符
# print(res.group(1))     #group(1)代表拿到的第一个字符

# s = 'hellolemonfixlemon'
# res = re.findall('lemon',s)
# print(res)      #列表形式返回匹配结果！不支持group！如果有分组，就以元祖的形式表现出来 列表嵌套元祖

s = '{"phone":"${normal_tel}","pwd":"${pwd}"}'
res = re.search('\$\{(.*?)\}',s)
# while re.search('\$\{(.*?)\}',s):
print(res.group())
print(res.group(1))
key = re.search('\$\{(.*?)\}',s).group(0)
value = re.search('\$\{(.*?)\}',s).group(1)
print(key,value)
new_s = s.replace(key,str(getattr(GetData,value)))
print(new_s)