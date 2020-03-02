#!usr/bin/env python
#-*- coding:utf-8 -*-

#UI Automator：UI自动化测试框架，安卓移动端app
#本机所在路径：C:\Users\17486\AppData\Local\adt-bundle-windows\sdk\tools\uiautomatorviewer.bat
#当设备在被执行程序或被其他工具使用时，可能会截图失败，因为设备只支持一个工具使用！

#提供了一系列api：执行ui测试在系统或者第三方app上面
#允许在被测设备上执行操作，比如打开系统设置菜单
#适合编写黑盒自动化测试

#框架的主要特点：
#1.元素定位：UI Automator Viewer.  扫描/分析待测应用的ui组件的图像工具
#2.元素操作：Accessing device state.  在目标设备和app上的各种操作
#3.元素识别：UI Automator APIs.  在多个应用程序中捕获和操作UI组件

# aapium-app页面元素定位
#1.通过id定位元素：resrouce-id
#例：driver.find_element_by_id("cn.haowu.agent:id/et_name").send_keys("16602159899")
#2.通过ClassName定位：classname
#例：driver.find_element_by_class_name("android.widget.Button")
#3.通过Accessibilityld定位：content-desc
#例：driver.find_element_by_accessibility_id("")
#4.通过AndroidUiAutomator定位
#例：driver.find_elements_by_android_uiautomator('new UiSelector().resrouseId("cn.haowu.agent:id/et_name")')
#5.通过xpath定位(app自动化中，能不用xpath就不用)
#例：driver.find_element_by_xpath("")

#通过AndroidUiAutomator定位
#使用UiAutomator中的UiSelector类来处理元素定位
#在appium库中获取元素的方法是：driver.find_elements_by_android_uiautomator()
#该方法的参数为UiSelector类定位元素的表达式：new UiSelector().函数名称("定位表达式")---实例化
#举例：new UiSelector().checkable(true) resrouseId("cn.haowu.agent:id/et_name")

#checkable元素：checkable(true)
#checked元素：checked(true)
#resrouce-id元素：resrouseId("cn.haowu.agent:id/et_name")
#class元素：className("android.widget.Button")
#text文本：
#text("登录")
#textContains("密码")
#textMatches("")  #正则
#textStartWith("")
#content-desc元素：
#description("登录")
#descriptionContains("密码")
#descriptionMatches("")  #正则
#descriptionStartWith("")
