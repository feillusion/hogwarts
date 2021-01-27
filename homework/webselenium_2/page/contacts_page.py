from time import sleep

from selenium.webdriver.common.by import By
from homework.webselenium_2.page.base_page import BasePage


class Contacts(BasePage):


    def create_party(self):
        self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//input[@class="qui_inputText ww_inputText" and @name="name"]').send_keys('B级')
        sleep(1)
        self.driver.find_element(By.XPATH,'//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//div[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]//a[@id="1688851994215435_anchor"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//a[@class="qui_btn ww_btn ww_btn_Blue"]').click()
        sleep(3)
        return Contacts(self.driver)

    def get_deptlist(self):
        webelements = self.driver.find_elements(By.XPATH,'//li[@class="jstree-node js_editable jstree-leaf jstree-last"]/a')
        dept_list = []
        for webelement in webelements:
            dept_list.append(webelement.text)
        return  dept_list
