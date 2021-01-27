from selenium.webdriver.common.by import By

from homework.webselenium_2.page.base_page import BasePage
from homework.webselenium_2.page.contacts_page import Contacts


class IndexPage(BasePage):

    def goto_contacts(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.ID,'menu_contacts').click()
        return Contacts(self.driver)
