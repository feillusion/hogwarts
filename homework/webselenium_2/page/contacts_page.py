from time import sleep
from homework.webselenium_2.page.base_page import BasePage


class Contacts(BasePage):


    def create_party(self,name):
        #操作之间间隔1s便于观察
        self.find('//i[@class="member_colLeft_top_addBtn"]').click()
        sleep(1)
        self.find('//a[@class="js_create_party"]').click()
        sleep(1)
        self.find('//input[@class="qui_inputText ww_inputText" and @name="name"]').send_keys(name)
        sleep(1)
        self.find('//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        sleep(1)
        self.find('//div[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]//a[@id="1688851994215435_anchor"]').click()
        sleep(1)
        self.find('//a[@class="qui_btn ww_btn ww_btn_Blue"]').click()
        #等待3s，确保列表数据刷新
        sleep(3)
        return Contacts(self.driver)

    def get_deptlist(self):
        webelements = self.finds('//li[@class="jstree-node js_editable jstree-leaf jstree-last"]/a')
        dept_list = []
        for webelement in webelements:
            dept_list.append(webelement.text)
        return  dept_list
