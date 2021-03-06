import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from homework.frame_1.find_blacklist import find_blacklist


class BasePage:
    def __init__(self,driver:webdriver = None):
        self.driver= driver

    #查找元素并返回
    @find_blacklist
    def find(self,locator):
        return self.driver.find_element(*locator)

    #查找多个元素并返回列表
    def finds(self,locator):
        return self.driver.find_elements(*locator)

    #查找元素并点击
    def click(self,locator):
        ele = self.find(locator)
        ele.click()

    #查找元素并输入文本
    def sendkeys(self,locator,keys):
        ele = self.find(locator)
        ele.send_keys(keys)

    #滚动查找指定文本的元素并点击
    def scroll_to_click(self,text):
        ele = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            f'.scrollIntoView(new UiSelector().text("{text}").instance(0));')
        ele.click()
