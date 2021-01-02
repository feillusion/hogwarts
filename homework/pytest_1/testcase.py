import pytest
import yaml
from homework.pytest_1 import calculator


class TestCase():
    def setup_class(self):
        self.cal = calculator.Calculator()
        print("-------测试开始-------")
    def teardown_class(self):
        print("-------测试结束-------")
    def setup(self):
        print("---开始计算---")
    def teardown(self):
        print("---计算结束---")

    #--------------------测试加法--------------------
    #获取数据
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("data.yaml"))["add"])
    def test_add(self,a,b,expect):
        result = self.cal.add(a,b)
        if result == expect:
            print(f"{a} + {b}的计算结果是{result}，预期值是{expect},测试通过")
        assert result == expect

    #--------------------测试除法--------------------
    #获取数据
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("data.yaml"))["div"])
    def test_div(self,a,b,expect):
        result = self.cal.div(a,b)
        if result == expect:
            print(f"{a} / {b}的计算结果是{result}，预期值是{expect},测试通过")
        assert result == expect

if __name__ == '__main__':
    pytest.main(["testcase.py"])