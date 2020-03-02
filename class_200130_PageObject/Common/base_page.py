#!usr/bin/env python
#-*- coding:utf-8 -*-

#封装基本函数--执行日志/异常处理/失败截图
#所有页面公共的非业务操作
import logging
import time,os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_200130_PageObject.Common.my_log import MyLog

class BasePage:
    """封装所有页面公共的非业务操作"""

    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_element_visible(self,locator,doc="",timeout=20):
        """
        :param locator: 元素定位（元祖形式）
        :param timeout: 等待时长，默认30s
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        MyLog().info('{0}页面等待{1}元素可见'.format(doc,locator))
        try:
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            #可增加记录等待时长的日志
        except:
            logging.exception('等待元素可见失败！')
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_element_exist(self,locator,doc="",timeout=30):
        """
            :param locator: 元素定位（元祖形式）
            :param timeout: 等待时长，默认30s
            :param doc: 模块名_页面名称_操作名称
            :return:
        """
        MyLog().info('{0}页面等待{1}元素存在'.format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            # 可增加记录等待时长的日志
        except:
            logging.exception('等待元素存在失败！')
            self.save_screenshot(doc)
            raise

    #截图
    def save_screenshot(self,doc):
        """
            :param doc: 模块名_页面名称_操作名称
        """
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Report/screenshot_photo/')
        screenshot_time = time.strftime('%Y-%m-%d %H_%M_%S')
        file_name = screenshot_dir + '{0}_{1}.png'.format(doc,screenshot_time)
        try:
            self.driver.save_screenshot(file_name)
            MyLog().info('截图成功，图片路径为{}'.format(file_name))
        except:
            MyLog().error('截图失败！')

    #查找元素
    def get_element(self,locator,doc=""):
        MyLog().info('{0}页面查找元素：{1}'.format(doc,locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败！')
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=""):
        element = self.get_element(locator,doc)
        MyLog().info('{0}页面点击元素：{1}'.format(doc,locator))
        try:
            element.click()
        except:
            logging.exception('点击操作失败！')
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        element = self.get_element(locator,doc)
        MyLog().info('{0}页面元素{1},输入{2}'.format(doc, locator,text))
        try:
            element.send_keys(text)
        except:
            logging.exception('输入操作失败！')
            self.save_screenshot(doc)
            raise

    #获取元素属性
    def get_element_attribute(self,locator,attribute,doc=""):
        element = self.get_element(locator, doc)
        MyLog().info('{0}页面获取元素{1}的{2}属性'.format(doc, locator,attribute))
        try:
            return element.get_attribute(attribute)
        except:
            logging.exception('获取元素属性失败！')
            self.save_screenshot(doc)
            raise

    # 获取元素文本内容
    def get_element_text(self, locator, doc=""):
        element = self.get_element(locator, doc)
        MyLog().info('{0}页面获取元素{1}的文本内容'.format(doc, locator))
        try:
            return element.text
        except:
            logging.exception('获取元素文本内容失败！')
            self.save_screenshot(doc)
            raise

    #等待alert弹框出现
    def wait_alert_exist(self,doc="",timeout=20):
        MyLog().info('{0}页面等待展示alert弹框'.format(doc))
        try:
            WebDriverWait(self.driver,timeout).until(EC.alert_is_present())
        except:
            logging.exception('等待alert弹框出现失败！')
            self.save_screenshot(doc)
            raise

    #alert处理
    def alert_operation(self,doc="",operation='accept'):
        MyLog().info('{0}页面处理alert弹框')
        try:
            alert = self.driver.switch_to.alert
            if operation == 'accept':
                alert.accept()
            elif operation == 'dismiss':
                alert.dismiss()
        except:
            logging.exception('处理alert弹框失败！')
            self.save_screenshot(doc)
            raise

    #iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    #上传操作
    def upload_file(self):
        pass

    #滚动条处理
    def scrollbar_operation(self):
        pass



