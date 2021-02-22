import pytest
import yaml

from homework.appium_2.page.app import APP


class  TestCases():
    def setup(self):
        self.main = APP().start_app()

    def teardown(self):
        self.main.stop_app()

    @pytest.mark.parametrize('name,sex,phone,deps,asserts',yaml.safe_load(open('test_datas.yaml',encoding='utf-8')))
    def test_add(self,name,sex,phone,deps,asserts):
        result = None
        if asserts == '已添加':
            result = self.main.goto_message().goto_contact().goto_addmember().manual_add()\
                .add_member(name,sex,phone,deps).already_toast()
        if asserts == '无效手机号':
            result = self.main.goto_message().goto_contact().goto_addmember().manual_add()\
                .add_member(name,sex,phone,deps).valid_toast()
        if asserts == '成功添加':
            result = self.main.goto_message().goto_contact().goto_addmember().manual_add() \
                .add_member(name, sex, phone, deps).success_toast()
        self.main.asserts(result,asserts)
