import pytest
import yaml

from homework.appium_1.page.message_page import MessagePage


class  TestCases():
    def setup(self):
        self.main = MessagePage()

    def teardown(self):
        self.main.quit()

    @pytest.mark.parametrize('name,sex,phone,deps,asserts',yaml.safe_load(open('test_datas.yaml',encoding='utf-8')))
    def test_add(self,name,sex,phone,deps,asserts):
        result = self.main.goto_contact().goto_addmember().manual_add().add_member(name,sex,phone,deps,asserts)
        self.main.asserts(result,asserts)
