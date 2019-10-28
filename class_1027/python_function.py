#!usr/bin/env python
#-*- coding:utf-8 -*-

#python内置函数
#特点：
#可以重复使用


#函数的语法：def 关键字
#函数名命名的规范：小写字母，不能以数字开头，不同的字母之间用下划线隔开
#def 函数名:
    #函数体（具体要实现的功能）

#调用：函数名()

def add_numbers():
    sum = 0
    for i in range(101):
        sum += i
    print("求和值是：{}".format(sum))
add_numbers()

#第一步：先用代码实现功能，还可以选取一组数据来证明是否正确
#第二步：变成函数，加def
#第三步：想办法提高代码的复用性

#默认参数，必须要放在位置参数的后面
def add_numbers(m,n,k=1):   #形参/位置参数，k=1是位置参数
    sum = 0
    for i in range(m,n,k):
        sum += i
    print("求和值是：{}".format(sum))
add_numbers(1,101)  #实参，默认情况下按顺序赋值

#return: 当你调用函数时，就会返回一个值，即return后面的表达式
#在函数中相当于一个结束符号，表示函数到此为止，后面的代码不会被执行
#什么时候用：当需要调用函数值的时候用return
def add_numbers(m,n,k=1):
    sum = 0
    for i in range(m,n,k):
        sum += i
    return sum

result = add_numbers(1,10)
print(result)

#写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def check_list(L):
    if len(L) > 2:
        new_list = L[0:2]
    return new_list
L = [1,2,3]
print(check_list(L))

#动态参数/不定长参数ix