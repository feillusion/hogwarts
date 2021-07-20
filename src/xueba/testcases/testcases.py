from time import sleep

from src.xueba.pages.loginpage import StartPage


class TestCases:
    def setup(self):
        self.app = StartPage()
    def teardown(self):
        sleep(3)
        self.app.driver.quit()

    def test_task(self):
        self.app.login().login_student().release_task()

    def test_search(self):
        print(self.app.login().login_student().goto_contact().goto_search().search().get_studentlist())

    def test_addfriend(self):
        self.app.login().login_student().goto_contact().goto_search().search().add_friend()