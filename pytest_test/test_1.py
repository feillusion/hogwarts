import pytest
import yaml


class TestCases1():

    def test_1(self):
        print("case1")

    def test_2(self):
        print("case2")

class TestCases2():

    def test_3(self):
        print("case3")

class TestCase3():

    def func(self,x):
        return x+1

    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_4(self,a,b):
        assert self.func(a) == b

    def test_5(self,show):
        print(f"test_5:{show}")

@pytest.fixture()
def show():
    print("haha")
    return "hi"
#python入口函数
if __name__ == "__main__":
    #pytest.main(["test_1.py"])
    pytest.main(["test_1.py::TestCases2"])