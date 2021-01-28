import pytest
import yaml

from homework.webselenium_2.page.index_page import IndexPage


class TestCases():
    def setup(self):
        #实例化一个首页
        self.main=IndexPage()

    def teardown(self):
        self.main.quit()

    @pytest.mark.parametrize('name',yaml.safe_load(open('party.yaml',encoding='utf-8')))
    def test_adddept(self,name):
        result = self.main.goto_contacts().create_party(name).get_deptlist()
        assert name in result