#!usr/bin/env python
#-*- coding:utf-8 -*-

#上传操作

#有2种情况：
#1.如果是input可以直接输入路径的，那么直接调send_keys()输入路径
#2.非input标签的上传，则需要借助第三方工具：
    #(1)AutoIt 我们去调用其生成的au3或exe文件
    #(2)Python pywin32库，识别对话框句柄，进而操作
    #(3)pyautoit库