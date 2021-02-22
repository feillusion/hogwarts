from homework.appium_2.page.base_page import BasePage
from homework.appium_2.page.contact_page import ContactPage


class MessagePage(BasePage):
    def goto_contact(self):
        self.click('//*[@text="通讯录" and @resource-id="com.tencent.wework:id/en5"]/../..')
        return ContactPage(self.driver)