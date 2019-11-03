#!usr/bin/env python
#-*- coding:utf-8 -*-

#1.设计一个登录程序，不同的用户名和对应的密码存在一个字典里面，输入正确的用户和密码去登录；
#paawd = {"admin": "111111", "user1": "222222"}
#2.首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名；
#3.当用户名正确时，提示去输入密码；如果密码和用户名不匹配，则提示密码错误请重新输入；
#4.如果密码输入错误超过3次，中断程序运行；
#5.当输入的密码错误时，提示还有几次机会；
#6.用户名和密码都输入成功时，提示登录成功。

# passwd = {"admin": "111111", "user1": "222222"}
# count = 3
# while True:
#     username = input('请输入用户名：')
#     if username in passwd.keys():
#         while count >0:
#             password = input('请输入密码：')
#             if password == passwd[username]:
#                 print("登录成功！")
#                 break
#             else:
#                 print("密码错误，请重新输入！")
#                 count -= 1
#                 print('你还有{}次机会！'.format(count))
#         break
#     # else:
#     elif username not in passwd.keys() or username == "":
#         print('请输入正确的用户名！')

#输入num为四位数，对其按照如下的规则进行加密：
#1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
#2）将该数的第一位和第4位互换，第二位和第三位互换
#3）最后合起来作为加密后的整数输出
num = input("请输入4位数字：")
new_num = ''
for item in num:
    new_num += str((int(item)+5)%10)
last_num = new_num[::-1]
print(last_num)