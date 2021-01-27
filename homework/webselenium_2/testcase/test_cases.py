from homework.webselenium_2.page.index_page import IndexPage


class TestCases():
    def setup(self):
        #实例化一个首页
        self.main=IndexPage()

    def teardonw(self):
        self.main.quit()

    def test_adddept(self):
        result = self.main.goto_contacts().create_party().get_deptlist()
        assert 'B级' in result