import pytest
import yaml

from homework.frame_2.app import APP


class  TestCases:
    def setup(self):
        self.main = APP().start_app()

    def teardown(self):
        self.main.stop_app()

    @pytest.mark.parametrize('search,click,asserts',yaml.safe_load(open('test_xueqiu.yaml',encoding='utf-8'))['test_search'])
    def test_search(self,search,click,asserts):
        result = self.main.goto_main().goto_market().goto_search().search(search,click).get_result()
        print(result)
        assert asserts in result