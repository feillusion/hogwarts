from homework.webselenium_2.page.base_page import BasePage
from homework.webselenium_2.page.contacts_page import Contacts


class IndexPage(BasePage):

    def goto_contacts(self):
        self.find('menu_contacts','id').click()
        return Contacts(self.driver)
