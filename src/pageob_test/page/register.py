from selenium.webdriver.common.by import By

from src.pageob_test.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("hehe")
        self.find(By.ID,"manager_name").send_keys("haha")
        return True