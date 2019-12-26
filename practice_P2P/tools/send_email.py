#!usr/bin/env python
#-*- coding:utf-8 -*-

import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

server = 'smtp.163.com'
sender = 'z16602159899@163.com'
passwd = 'zyj16602159899'

now = time.strftime('%Y-%m-%d %H:%M:%S')

class SendEmail:
    """封装邮件发送类"""
    def send_email(self,receivers,filepath):
        #receivers:收件人
        #filepath:发放附件的地址
        msg = MIMEMultipart()       #如名字所示，Multipart就是分多个部分
        msg["Subject"] = now + "测试报告"
        msg["From"] = sender
        msg["To"] = receivers

        #文字部分
        content = MIMEText("这次的自动化测试结果，请查收！")
        msg.attach(content)

        #附件部分(只能发送一个附件)
        content = MIMEApplication(open(filepath,'rb').read())
        content.add_header('Content-Disposition','attachment',filename=filepath)
        msg.attach(content)

        #发放邮件
        smtp = smtplib.SMTP_SSL(server,timeout=30)       #连接smtp邮件服务器
        smtp.login(sender,passwd)                               #登录服务器
        smtp.sendmail(sender,receivers,msg.as_string())         #发放邮件
        smtp.close()

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__),'image.jpg')
    SendEmail().send_email('1174066702@qq.com',file_path)