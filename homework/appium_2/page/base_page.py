import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    def __init__(self,driver:webdriver = None):
        self.driver= driver

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

    def asserts(self,results,key):
        rel = {}
        with open('../page/asserts.json','r',encoding='utf-8') as f:
            rel = json.load(f)
        assert results == rel[key]