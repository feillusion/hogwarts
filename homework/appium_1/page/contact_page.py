from homework.appium_1.page.addmember_page import AddMember
from homework.appium_1.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_addmember(self):
        self.click('//*[@class="android.widget.TextView" and @text="添加成员"]/../../../../..')
        return AddMember(self.driver)