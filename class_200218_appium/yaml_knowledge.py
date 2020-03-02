#!usr/bin/env python
#-*- coding:utf-8 -*-

# Yaml语言
#是一种简洁的非标记语言
#Yaml以数据为中心，使用空白/缩进/分行组织数据，从而使得表示更加简洁易懂

#基本规则：
#1.大小写敏感
#2.使用缩进表示层级关系
#3.禁止使用tab缩进，只能使用空格键
#4.缩进长度没有限制，只要元素对齐就表示这些元素属于一个层级
#5.使用#表示注释
#6.字符串可以不用引号标注

#三种数据结构：
#1.字典
#使用冒号（：）表示键值对，同一缩进的所有键值属于一个map
#方式一（注意冒号后的空格）：platformVersion: 5.1
#方式二：{platformVersion: 5.1,platformName: Android}

#2.列表
#使用连字符（-）表示，注意-后的空格
#方式一：- help
#方式二：[hello,world,22,33]

#3.scalar,纯量

#如何读取？
#python库：PyYAML/ruamel.yaml
#命令：pip install PyYaml
#引入：import yaml
#读取yaml文件的数据，并转换成python对象
#1.打开yaml文件
#2.使用yaml的load()函数

#示例：
#fs = open(caps.yaml)
#datas = yaml.load(fs)
