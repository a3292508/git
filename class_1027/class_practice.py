#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#打印九九乘法表
# for i in range(1,10):         #控制行数
#     for j in range(1,i+1):    #控制每一行里的变化
#         print('{0}*{1}={2}\t'.format(j,i,j*i),end='')
#     print('\n')

# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (j, i, i*j))

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and i != k and j != k:
#                 print(i,'',j,'',k)

#输入三个整数x,y,z，请把这三个数由小到大输出
# list_01 = []
# for i in range(3):
#     x = int(input('请输入整数：'))
#     list_01.append(x)
# list_01.sort()
# print(list_01)

#斐波那契数列
#0,1,1,2,3,5,8,13,21,34,55......
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
#
# print(fib(10))

# l = [1,2,3,4]
# ll = l[::-1]
# print(ll)

# 判断101-200之间有多少个素数，并列表输出所有素数
# l = []
# for i in range(101,200):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         # print('{}是素数'.format(i))
#         l.append(i)
# print(l)

# 打印出所有的"水仙花数"
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
# for n in range(100,1000):
#     i = n//100
#     j = n//10%10
#     k = n%10
#     if n == i**3 + j**3 + k**3:
#         print(n)
#
# print(888//100)

#冒泡排序   两两比较，一般最多比较n-1次就完成
# list = [1,30,22,225,66,51,900]
# for i in range(len(list)-1):
#     for j in range(len(list)-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
#     print(list)

