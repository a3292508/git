#!usr/bin/env python
#-*- coding:utf-8 -*-

#微信小程序自动化

#QQ/微信都是基于腾讯自研X5内核，一般的模拟器来调试自动化代码会有问题，因此最好用一台真实的手机来做。
#X5内核应用自动化方式和普通混合应用有非常多的差异。
#准备工作：
#1.java-client5.0.3依赖包
#2.微信应用版本6.7.2
#3.科学上网工具（或者uc-devtools）
#4.手机端和PC端安装chrome浏览器（注意版本最好一致）
#5.Android手机（5.0+版本）
#6.chromedriver2.26
#7.appium-desktop V1.5.0

#步骤：
#1.打开微信，在任意窗口输入：debugx5.qq.com
#2.在打开的界面中选择信息->勾选“是否打开TBS内核inspector调试功能”
#3.手机通过usb连接到电脑，打开USB调试模式，通过adb devices命令检测到设备
#4.打开微信->发现->搜一搜，搜索相应小程序，点击对应小程序进入到主页面
#5.在chrome浏览器里输入chrome://inspect#devices.显示的webview版本是微信X5内核的版本，不是Android System webview版本。
#注意事项：
#（1）.页面空白加载不出来，因为google的inspect工具需要访问墙外的网站，需要有翻墙工具或者VPN方式
#（2）.微信在新版本中对小程序调试入口加上了限制：在微信主窗口下打开小程序，在chrome中通过inspect工具是检测不到小程序对应的url入口的，需
#要在微信->发现->搜一搜，搜索相应小程序
#（3）.如果点击右上角关闭了小程序之后，一定要记得从后台清理下对应的小程序进程（关闭之后小程序还在后台运行），再次点击重启小程序
#6.默认appium-desktop安装之后里面自带的chromedriver不是2.26的，需要手动去官网下载对应版本，并放到appium的chromedriver对应目录中
#7.微信/qq有很多的进程，我们要确定当前web是位于哪个进程中。
# 执行命令：adb shell dumpsys activity top |findstr ACTIVITY       --->获取进程的pid
# 再执行命令：adb shell ps 进程的pid         --->确定当前微信的页面运行在哪个进程中
#8.desired_caps中指定recreateChromeDriverSessions = true(默认是false)--->desired_caps["recreateChromeDriverSessions"]=True
#9.desired_caps中指定chromeOptions = {"androidPrecess":"com.tencent.mm:toolsmp"}
#10.desired_caps中指定browserName = ""
