#!usr/bin/env python
#-*- coding:utf-8 -*-

#appium的一些基本操作

#1.滑动屏幕
# 原理：
#1.先获取设备的屏幕大小（长/宽）
#2.再设置滑动的距离与屏幕大小的百分比
#3.调用滑动接口执行滑动操作

#滑动接口：swipe(起始X，起始Y，结束X，结束Y)
#结束X-起始X：X轴滑动的距离
#结束Y-起始Y：Y轴滑动的距离

#获取当前窗口大小的接口，返回窗口的宽和高：get_window_size()

#2.模拟触屏（手势密码绘制常用，因机型得分辨率不同，尽量使用坐标相对定位！！！）
#TouchAction类：将一系列的动作放在一个链条中，然后将该链条传递给服务器。服务器接收到该链条后，解析各个动作，逐个执行。
#from appium.webdriver.common.touch_action import TouchAction
#短按：press       一般和释放：release一起使用
#长按：longPress
#点击：tap
#移动到：move_to(x,y)       x,y为相对上一个坐标的移动距离
#等待：wait
#释放：release
#执行：perform
#取消：cancel
# 用法：
# TouchAction(driver).press(x="",y="").wait(200)\
#             .move_to(x="",y="").wait(200)\
#             .move_to(x="",y="").wait(200)\
#             .move_to(x="",y="").wait(200)\
#             .release()\
#             .perform()

#3.toast提示信息获取
#要获取toast需要满足以下4个要求：
#1.appium server版本1.6.3+才支持toast获取--->desired_caps["automationName"] = "UiAutomator2"
#2.代码中必须指定automationName为：UIAutomator2
#3.UIAutomator2只支持安卓版本5.0+
#4.要求按照JDK1.8 64位及以上。配置其环境变量JAVA_HOME和path

#1.xpath表达式：xpath = '//*[contains(@text,"部分文本内容")]'
#注意：driverWait方法中，请用prensence_of_element_located，不能用visibility_of_element_located，因为对toast的可见处理不支持！