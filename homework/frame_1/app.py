from time import sleep

from appium import webdriver

from homework.frame_1.base_page import BasePage
from homework.frame_1.page.main_page import MainPage


class APP(BasePage):
    def start_app(self):
        if self.driver is None:
            self.caps = {
                "platformName": "Android",
                "deviceName": "xueqiu",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                # 不清空本地缓存，启动app
                "noReset": "true",
                # 设置页面等待空闲状态的时间为0秒
                'settings[waitForIdleTimeout]': 3
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
            self.driver.implicitly_wait(30)
        else:
            self.driver.launch_app()
        return self

    def stop_app(self):
        sleep(5)
        self.driver.quit()
        return self

    def goto_main(self):
        return  MainPage(self.driver)
