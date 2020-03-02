#!usr/bin/env python
#-*- coding:utf-8 -*-

#混合应用（原生&H5）

#怎样分辨一个app页面究竟是native还是web？
#1.在手机/模拟器中点击关于手机中的版本号5下，打开开发者选项
#2.在开发者选项中勾选“显示布局边界”，再返回到app页面
#3.如果app是web页面，那界面不会有布局边界显示，如有则说明是native页面
#4.或者通过定位工具，查看页面的class元素，如果是WebView，则说明是web页面

#hybird混合应用自动化方案：
#基于UiAutomator+Chromedriver
#native部分走uiautomator，webview部分chromedriver，二者结合
#要求：
#1.Android 4.4+
#2.webview必须位debug版本

#获取webview页面的四种方式：
#1.在谷歌浏览器中输入chrome://inspect(推荐，可能需要翻墙！)
#2.使用driver.page_source获取html页面
#3.找开发人员要源文件
#4.uc-devtools不需要翻墙！（推荐！需要下载uc-devtools文件）

#常见问题：
#contexts只能获取NATIVE_APP,无法获取WEBVIEW
#使用uiautomatorviewer定位元素，显示class值为：android.webkit.WebView。但是driver.contexts只打印出了'NATIVE_APP'
#解决方法：
#1.app打包的时候需要开启webview的debug属性setWebContentDebuggingEnabled(true),直接让开发加上就好
#2.模拟器的contexts中有webview，但有些真机没有。需要将手机root，然后再去获取

#上下文（窗口）切换
#可用的上下文（Contexts）
#列出所有可用的上下文：driver.contexts
#当前上下文：driver.window.handles
#列出当前的上下文（窗口）：driver.current_context
#切换到默认的上下文：driver.switch_to.context(None)
#获取当前的Activity(仅支持安卓)：driver.current_activity
#获取当前的package(仅支持安卓)：driver.current_package