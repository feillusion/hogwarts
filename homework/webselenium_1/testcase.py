from time import sleep

from selenium import webdriver
import pytest
import json


class TestFuyong:

    # ！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 需提前关闭浏览器，并在安装路径使用命令开始调试窗口并登录
    # chrome --remote-debugging-port=9222
    # (9222为端口号，可以换成任意一个没有被占用的端口)
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 记录一下登录cookie，后续使用
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)
        self.driver.find_element_by_id('menu_customer').click()
        a = self.driver.find_element_by_xpath(
            "//a[@class='qui_tabNav_itemLink ww_tabNav_itemLink js_tabNav_itemLink js_sgkvuin_report_click']")
        assert a.text == '客户'


class TestCookies:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        #打开页面，写入需要的cookies
        self.driver.get('https://work.weixin.qq.com/')
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(1)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_case(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(1)
        self.driver.find_element_by_id('menu_customer').click()
        a = self.driver.find_element_by_xpath(
            "//a[@class='qui_tabNav_itemLink ww_tabNav_itemLink js_tabNav_itemLink js_sgkvuin_report_click']")
        assert a.text == '客户'


if __name__ == "__main__":
    pytest.main()
