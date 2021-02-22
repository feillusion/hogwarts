from appium import webdriver

from homework.appium_2.page.base_page import BasePage
from homework.appium_2.page.message_page import MessagePage


class APP(BasePage):
    def start_app(self):
        if self.driver is None:
            self.caps = {
                "platformName": "Android",
                "deviceName": "qiyeweixin",
                "appPackage": "com.tencent.wework",
                "appActivity": "launch.WwMainActivity",
                # 不清空本地缓存，启动app
                "noReset": "true",
                # 设置页面等待空闲状态的时间为0秒
                'settings[waitForIdleTimeout]': 0
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
            self.driver.implicitly_wait(30)
        else:
            self.driver.launch_app()
        return self

    def stop_app(self):
        self.driver.quit()
        return self

    def goto_message(self):
        return  MessagePage(self.driver)
