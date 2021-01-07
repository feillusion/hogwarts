from time import sleep

from selenium import webdriver
from src.selenium_test.base import Base

class TestSwitch(Base):

    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        first_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath("//a[@class='s-top-login-btn c-btn c-btn-primary c-btn-mini lb']").click()
        self.driver.find_element_by_css_selector("a[class='pass-reglink pass-link']").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(1)
        self.driver.find_element_by_name("userName").send_keys("aaaaa")
        self.driver.switch_to.window(first_window)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_name("password").send_keys("123444")

    def test_frame(self):
        pass