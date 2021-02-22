from homework.appium_2.page.addmember_page import AddMember
from homework.appium_2.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_addmember(self):
        add = self.find(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));',
            'uiautomator')
        add.click()
        return AddMember(self.driver)