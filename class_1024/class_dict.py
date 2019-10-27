#!usr/bin/env python
#-*- coding:utf-8 -*-

#字典，dict，符号{}
#1.可以存在空字典{}
#2.字典里数据的存储方式，key:value
#3.字典里面可以包含任何类型的数据
#4.字典里面的元素，用逗号来进行分隔
#5.字典是无序的，所以没有索引值（下标）
#6.字典里的key必须是唯一的（如果写多个，以最后一个为主）

dict_01 = {
    'class':'python',
    'student':'zhu',
    'score':100,
    'sub':['list','tuple','dict']
}
#字典取值，指明所取值的key
print(dict_01['score'])
#删除值，指明删除值的key
res = dict_01.pop('student')
print(res)
print(dict_01)
#新增值，key是字典中没有的
dict_01['age'] = 28
print(dict_01)
#修改值
dict_01['class'] = 'python11'
print(dict_01)
#只打印key值
print(dict_01.keys())
#只打印value值
print(dict_01.values())