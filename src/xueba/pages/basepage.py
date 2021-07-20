from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,base_driver:WebDriver=None):
        #如果传入了driver就使用传入的，没有的话就新建一个
        if base_driver is None:
            self.caps = {
                "platformName":"android",
                "deviceName":"mumu",
                "appPackage":"com.xiaoyu.com.xueba",
                "appActivity":"com.xiaoyu.jyxb.common.activity.LoginRegisterChooseActivity",
                # 清空本地缓存，启动app
                "noReset": "true",
                # 设置页面等待空闲状态的时间为0秒
                "settings[waitForIdleTimeout]": 0,
                # 设置编码格式支持中文并在结束后重置编码格式
                "unicodeKeyBoard": True,
                "resetKeyBoard": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub",self.caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def finds(self,locator):
        return self.driver.find_elements(*locator)

    def click(self,locator):
        self.find(locator).click()

    def sendkeys(self,locator,keys):
        self.find(locator).send_keys(keys)

    def cleantext(self,locator):
        self.find(locator).clear()