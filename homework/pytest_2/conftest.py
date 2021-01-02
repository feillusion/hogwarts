import allure
import pytest
import yaml
from homework.pytest_2 import calculator
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/data.yaml"
# 获取全部数据
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)

#加法数据参数化
@pytest.fixture(params=datas["add"],scope="module")
@allure.story("获取加法数据")
def get_add_datas(request):
    add_datas = request.param
    yield  add_datas

#减法数据参数化
@pytest.fixture(params=datas["sub"],scope="module")
@allure.story("获取减法数据")
def get_sub_datas(request):
    sub_datas = request.param
    yield  sub_datas

#乘法数据参数化
@pytest.fixture(params=datas["mul"],scope="module")
@allure.story("获取乘法数据")
def get_mul_datas(request):
    mul_datas = request.param
    yield  mul_datas

#除法数据参数化
@pytest.fixture(params=datas["div"],scope="module")
@allure.story("获取除法数据")
def get_div_datas(request):
    div_datas = request.param
    yield  div_datas

@pytest.fixture(autouse=True)
def fix_method():
    print("-----开始计算-----")
    yield
    print("-----计算结束-----")

@pytest.fixture(scope="module")
def fix_module():
    with allure.step("生成计算器实例"):
        cal = calculator.Calculator()
    print("--------------------测试开始--------------------")
    yield cal
    print("--------------------测试结束--------------------")

