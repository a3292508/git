#!usr/bin/env python
#-*- coding:utf-8 -*-

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_auto.Common.my_logger import MyLogger
from web_auto.Common.project_path import screenshot_dir

class BasePage:
    """封装所有页面公共的非业务操作"""

    def __init__(self,driver):
        self.driver = driver

    def save_screenshot(self):
        """保存截图"""
        screenshot_time = time.strftime('%Y-%m-%d %H_%M_%S')                    #截图的时间
        file_name = screenshot_dir + '{0}.png'.format(screenshot_time)     #截图保存的路径和名称
        try:
            self.driver.save_screenshot(file_name)
            MyLogger().info('截图成功，图片路径为{0}'.format(file_name))
        except:
            MyLogger().error('截图失败！')

    def wait_element_visible(self,locator,timeout=20):
        """等待元素可见"""
        MyLogger().info('等待{0}元素可见'.format(locator))
        try:
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        except:
            self.save_screenshot()
            MyLogger().error('等待元素可见失败！')
            raise

    def wait_element_present(self,locator,timeout=20):
        """等待元素存在"""
        MyLogger().info('等待{0}元素存在'.format(locator))
        try:
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except:
            self.save_screenshot()
            MyLogger().error('等待元素存在失败！')
            raise

    def get_element(self,locator):
        """查找元素"""
        MyLogger().info('查找元素：{0}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            self.save_screenshot()
            MyLogger().error('查找元素失败！')
            raise

    def click_element(self,locator):
        """点击元素操作"""
        MyLogger().info('点击元素{0}'.format(locator))
        element = self.get_element(locator)
        try:
            element.click()
        except:
            self.save_screenshot()
            MyLogger().error('点击元素失败！')
            raise

    def input_text(self,locator,text):
        """输入文本操作"""
        MyLogger().info('元素{0}输入{1}'.format(locator,text))
        element = self.get_element(locator)
        try:
            element.send_keys(text)
        except:
            self.save_screenshot()
            MyLogger().error('输入文本失败！')
            raise

    def get_element_attribute(self,locator,attribute):
        """获取元素属性"""
        MyLogger().info('获取元素{0}的{1}属性'.format(locator,attribute))
        element = self.get_element(locator)
        try:
            return element.get_attribute(attribute)
        except:
            self.save_screenshot()
            MyLogger().error('获取元素属性失败！')
            raise

    def get_element_text(self,locator):
        """获取元素文本内容"""
        MyLogger().info('获取元素{0}的文本内容'.format(locator))
        element = self.get_element(locator)
        try:
            return element.text
        except:
            self.save_screenshot()
            MyLogger().error('获取元素文本内容失败！')
            raise

    def wait_alert_visible(self,timeout=20):
        """等待alert弹框出现"""
        MyLogger().info('等待alert弹框出现')
        try:
            WebDriverWait(self.driver,timeout).until(EC.alert_is_present())
        except:
            self.save_screenshot()
            MyLogger().error('等待alert弹框出现失败！')
            raise

    def alert_operation(self,operation='accept'):
        """alert处理操作，默认同意"""
        MyLogger().info('alert弹框处理')
        try:
            alert = self.driver.switch.to_alert
            if operation == 'accept':
                alert.accept()
            elif operation == 'dismiss':
                alert.dismiss()
        except:
            self.save_screenshot()
            MyLogger().error('alert弹框处理失败！')
            raise

    def switch_iframe(self,iframe_name,timeout=20):
        """iframe切换操作"""
        MyLogger().info('元素{0}操作iframe切换'.format(iframe_name))
        try:
            WebDriverWait(self.driver,timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_name))
        except:
            self.save_screenshot()
            MyLogger().error('iframe切换失败！')
            raise

    def scrollbar_operation(self):
        """滚动条处理--移动到页面底部"""
        MyLogger().info('将滚动条移动到页面底部')
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            self.save_screenshot()
            MyLogger().error('滚动条移动到页面底部失败！')
            raise