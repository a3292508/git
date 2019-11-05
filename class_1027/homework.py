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

# num = input("请输入4位数字：")
# new_num = ''
# for item in num:
#     new_num += str((int(item)+5)%10)
# last_num = new_num[::-1]
# print(last_num)

#用*号输出一个直角三角形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print('')   #print语句会换行

#用*号输出一个等边三角形，每个边都是5个*
# for i in range(1,6):        #控制行数
#     for j in range(1,6-i):  #控制空格的数量
#         print(" ",end='')
#     for k in range(1,i+1):  #控制*号的数量
#         print('* ',end='')
#     print('')

#自动售卖机：只接受1元，5元，10元的纸币或硬币
#可以1块，5块，10块。最多不超过10元。
#饮料只有橙汁，椰汁，矿泉水，早餐奶，售价分别为3.5,4,2,4.5
#写一个函数用来表示贩卖机的功能：
#用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
def buy_drink():
    drinks = {"1":3.5,"2":4,"3":2,"4":4.5}
    total = 0
    while True:
        choose = input("请输入你要购买的饮料： 1：橙汁 2：椰汁 3：矿泉水 4：早餐奶 q：退出")
        if choose in drinks.keys():
            total += drinks[choose]
        elif choose == 'q':
            print("退出选择饮料")
            break
        else:
            print("不存在该选项，请重新选择！")

    toubi = 0
    while True:
        money = input("请投币：只能投1 5 10元面值的硬币或纸币，按q退出投币！")
        if money == '1' or money == '5' or money == '10':
            toubi += int(money)
            if toubi > total:
                print('您刚购买了{0}元饮料，已支付{1}元，找零{2}'.format(total,toubi,toubi-total))
                break
            elif toubi < total:
                print('您刚购买了{0}元饮料，已支付{1}元，仍需支付{2}'.format(total,toubi,total-toubi))
            else:
                print('您刚购买了{0}元饮料，已支付{1}元，已支付完毕！'.format(total, toubi))
                break
        elif money == 'q':
            print('退出投币')
            break
        else:
            print('你输入的选项不存在！')

buy_drink()