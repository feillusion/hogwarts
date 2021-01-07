from selenium import webdriver
import os


class Base:
    def setup_class(self):
        browser = os.getenv("browser")
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)


    def teardown_class(self):
        pass