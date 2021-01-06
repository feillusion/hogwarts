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

class TestHogwards:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        #self.driver.quit()
        pass

    def test_1(self):
        self.driver.get("http://houtai-test.dzxw.vip/index")
        sleep(3)
        self.driver.find_element_by_xpath("//*/input[@class='el-input__inner' and @placeholder='请输入手机号']").send_keys("15624008720")
        self.driver.find_element_by_xpath("//*/input[@class='el-input__inner' and @placeholder='密码']").send_keys("15624008720")
        self.driver.find_element_by_xpath("//*/span[@class='el-checkbox__inner']").click()
        self.driver.find_element_by_xpath("//*/button[@class='el-button el-button--primary el-button--medium']").click()

if __name__ == "__main__":
    pytest.main(["test_1.py","-s"])