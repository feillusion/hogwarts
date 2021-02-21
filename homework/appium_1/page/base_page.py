import json

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,base_driver=None):
        self.caps={
                "platformName"  :   "Android",
                "deviceName"    :   "qiyeweixin",
                "appPackage"    :   "com.tencent.wework",
                "appActivity"   :   "launch.WwMainActivity",
                # 不清空本地缓存，启动app
                "noReset"       :   "true",
                # 设置页面等待空闲状态的时间为0秒
                'settings[waitForIdleTimeout]': 0
        }
        base_driver:WebDriver
        if base_driver is None:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
            self.driver.implicitly_wait(30)
        else:
            self.driver = base_driver

    def find(self,locator,By='xpath'):
        if 'id' in By:
            return self.driver.find_element(MobileBy.ID,locator)
        elif 'css' in By:
            return self.driver.find_element(MobileBy.CSS_SELECTOR,locator)
        elif 'uiautomator' in By:
            return self.driver.find_element_by_android_uiautomator(locator)
        else:
            return self.driver.find_element(MobileBy.XPATH,locator)

    def finds(self,locator,By='xpath'):
        if 'id' in By:
            return self.driver.find_elements(MobileBy.ID,locator)
        elif 'css' in By:
            return self.driver.find_elements(MobileBy.CSS_SELECTOR,locator)
        else:
            return self.driver.find_elements(MobileBy.XPATH,locator)

    def click(self,locator,By='xpath'):
        ele = self.find(locator,By)
        ele.click()

    def sendkeys(self,locator,keys,By='xpath'):
        ele = self.find(locator,By)
        ele.send_keys(keys)

    def quit(self):
        self.driver.quit()

    def asserts(self,results,key):
        rel = {}
        with open('../page/asserts.json','r',encoding='utf-8') as f:
            rel = json.load(f)
        assert results == rel[key]