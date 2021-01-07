from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# class TestWebdriver:
#
#     def setup(self):
#         sleep(3)
#
#     def teardown(self):
#         sleep(3)
#         self.driver.quit()
#
#     def test_chrome(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://www.baidu.com")
#
#     def test_firefox(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.baidu.com")

class TestMy:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        #self.driver.quit()
        pass

    def setup(self):
        self.driver.get("http://houtai-test.dzxw.vip/index")
        sleep(3)

    def teardown(self):
        sleep(3)

    def test_xpath(self):
        self.driver.find_element_by_xpath("//input[@class='el-input__inner' and @placeholder='请输入手机号']").send_keys("10023456789")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@class='el-input__inner' and @placeholder='密码']").send_keys("666666")
        sleep(1)
        self.driver.find_element_by_xpath("//span[@class='el-checkbox__inner']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--medium']").click()

    def test_cssselector(self):
        self.driver.find_element_by_css_selector(".el-input__inner[placeholder='请输入手机号']").send_keys("10023456789")
        sleep(1)
        self.driver.find_element_by_css_selector(".el-input__inner[placeholder='请输入手机号']").clear()
        sleep(1)
        self.driver.find_element_by_css_selector(".el-input__inner[placeholder='请输入手机号']").send_keys("12345678900")
        sleep(1)
        self.driver.find_element_by_css_selector(".el-input__inner[placeholder='密码']").send_keys("666666")
        self.driver.find_element_by_css_selector(".el-input__inner[placeholder='验证码']").send_keys("abcd")
        sleep(1)
        self.driver.find_element_by_css_selector(".el-checkbox__inner").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[class='el-button el-button--primary el-button--medium']").click()

if __name__ == "__main__":
    pytest.main(["test_1.py","-s"])