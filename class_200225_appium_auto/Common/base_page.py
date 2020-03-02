#!usr/bin/env python
#-*- coding:utf-8 -*-

import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_200225_appium_auto.Common.my_logger import MyLogger
from class_200225_appium_auto.Common.project_path import screenshot_dir

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

    #上下左右滑动
    def swipe_up(self,size):
        """向上滑动"""
        MyLogger().info('向上滑动')
        size = self.get_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.7
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.2
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)


    def swipe_down(self,size):
        """向下滑动"""
        MyLogger().info('向下滑动')
        size = self.get_size()
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.2
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.7
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    def swipe_left(self,size):
        """向左滑动"""
        MyLogger().info('向左滑动')
        size = self.get_size()
        start_x = size["width"] * 0.8
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.1
        end_y = size["height"] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    def swipe_right(self,size):
        MyLogger().info('向右滑动')
        """向右滑动"""
        size = self.get_size()
        start_x = size["width"] * 0.1
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.8
        end_y = size["height"] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    def get_size(self):
        """获取屏幕大小"""
        MyLogger().info('获取屏幕大小')
        try:
            return self.driver.get_window_size()
        except:
            self.save_screenshot()
            MyLogger().error('获取屏幕大小失败！')
            raise

    def get_toast_message(self,text):
        """获取toast信息"""
        loc = '//*[contains(text,"{0}")]'.format(text)
        try:
            WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH,loc)))
            return self.driver.find_element_by_xpath(loc).text
        except:
            self.save_screenshot()
            MyLogger().error("没有找到匹配的toast！")
            raise

    #H5切换
    def switch_to_H5(self):
        """切换到H5页面"""
        pass

    def switch_to_native(self):
        """切换到原生页面"""
        pass
