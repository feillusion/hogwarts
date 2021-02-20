from appium.webdriver import webdriver


class BasePage:
    def setup(self):
        self.caps={
                "platformName"  :   "Android",
                "deviceName"    :   "device",
                "appPackage"    :   "com.xueqiu.android",
                "appActivity"   :   ".common.MainActivity",
                # 不清空本地缓存，启动app
                "noReset"       :   "true",
                # 设置页面等待空闲状态的时间为0秒
                'settings[waitForIdleTimeout]': 0
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        self.driver.implicitly_wait(60)

    def teardown(self):
        self.driver.quit()