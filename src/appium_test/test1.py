from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium:

    def setup(self):
        self.caps = {}
        self.caps["platformName"] = "Android"
        self.caps["deviceName"] = "device"
        self.caps["appPackage"] = "com.xueqiu.android"
        self.caps["appActivity"] = ".common.MainActivity"
        # 不清空本地缓存，启动app
        self.caps["noReset"] = "true"
        self.caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        self.caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        self.driver.implicitly_wait(60)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_search(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        sleep(3)
        el2.click()
        el3 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='阿里巴巴']/../..")
        el3.click()
        el4 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BABA']/../../..//android.widget.TextView[@resource-id='com.xueqiu.android:id/current_price']")
        currect_price = float(el4.text)
        # print(el4.size)
        # print(el4.location)
        # print(currect_price)
        assert  currect_price > 200

    def test_action(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        x = int(float(width)/2)
        y_start = int(float(height)*4/5)
        y_mid = int(float(height)/2)
        y_end = int(float(height)/5)
        print(x,y_start,y_mid,y_end)
        locator = (MobileBy.XPATH,"//android.widget.TextView[@text='推荐']/../../..")
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        sleep(3)
        TouchAction(self.driver).press(x=x,y=y_start).move_to(x=x,y=y_mid).wait(3000).move_to(x=x,y=y_end).release().wait(3000).perform()
        sleep(5)

