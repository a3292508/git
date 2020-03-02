#!usr/bin/env python
#-*- coding:utf-8 -*-

#adb:是Android sdk的一个工具
#adb是用来连接安卓收集和PC端的桥梁，要有adb作为二者之间的维系，才能让用户在电脑上对手机进行全面的操作。
#Android的初衷是用adb这样的一个工具来协助开发人员在开发Android应用的过程中更快更好的调试apk，因此adb具有安装卸载apk/拷贝推送
#文件/查看设备硬件信息/查看应用程序占用资源/在设备执行shell命令等功能。

#adb常见命令：
#adb -help 查看帮助手册
#adb devices  检查连接到电脑的安卓设备（经常用到的检测命令）
#adb logcat  打印log信息
#adb logcat > D:\adb.logcat.txt  将adb的日志打印到指定文件
#adb pull <手机路径> <本机路径>  从手机中拉取信息放到本地电脑上
#adb push <本机路径> <手机路径>  从本地推送信息到手机上去
#adb shell 登录设备shell（命令行的人机界面），ll ls等命令都可以使用，进入到linux命令环境了，相当于执行远程命令
#adb install D:\xxx.apk 为了获取apk的安装包所在地址，可以直接把apk拖到cmd的窗口获取，返回success就代表安装成功
#adb uninstall cn.haowu.agent   --应用包名
#adb shell dumpsys activity | find "mFocusedActivity"  --查看前台在运行的应用activity名
#adb kill-server  终止adb服务
#adb start-server  启动adb服务。通常在adb遇到问题时，与adb kill-server一起使用
#adb shell pm list packages  列出所有包名
#-f 列出所有apk路径及包名
#-s 列出系统apk路径及包名
#-3 列出用户apk路径及包名


