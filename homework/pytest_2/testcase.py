import allure
import pytest


# --------------------测试加法--------------------
class TestAdd():
    def setup_class(self):
        print("------------测试加法------------")

    @pytest.mark.flaky(reruns=2)
    @allure.story('加法测试')
    @pytest.mark.run(order=1)
    def test_add(self,get_add_datas,fix_module):
        result = None
        try:
            result = fix_module.add(get_add_datas[0],get_add_datas[1])
            if result == get_add_datas[2]:
                print(f"{get_add_datas[0]} + {get_add_datas[1]}的计算结果是{result}，预期值是{get_add_datas[2]},测试通过")
        except Exception as e:
            print(e)
        finally:
            with allure.step("加法验证"):
                pytest.assume(result == get_add_datas[2])

#--------------------测试除法--------------------
class TestDiv():
    def setup_class(self):
        print("------------测试除法------------")

    @pytest.mark.flaky(reruns=5, reruns_delay=3)
    @allure.story('除法测试')
    @pytest.mark.run(order=4)
    def test_div(self,get_div_datas,fix_module):
        result = None
        try:
            result = fix_module.div(get_div_datas[0],get_div_datas[1])
            if result == get_div_datas[2]:
                print(f"{get_div_datas[0]} / {get_div_datas[1]}的计算结果是{result}，预期值是{get_div_datas[2]},测试通过")
        except Exception as e:
            print(e)
        finally:
            with allure.step("除法验证"):
                pytest.assume(result == get_div_datas[2])

#--------------------测试减法--------------------
class TestSub():
    def setup_class(self):
        print("------------测试减法------------")

    @allure.story('减法测试')
    @pytest.mark.run(order=2)
    def test_sub(self,get_sub_datas,fix_module):
        result = None
        try:
            result = fix_module.sub(get_sub_datas[0],get_sub_datas[1])
            if isinstance(result,float):
                result = round(result,2)
            if result == get_sub_datas[2]:
                print(f"{get_sub_datas[0]} - {get_sub_datas[1]}的计算结果是{result}，预期值是{get_sub_datas[2]},测试通过")
        except Exception as e:
            print(e)
        finally:
            with allure.step("减法验证"):
                pytest.assume(result==get_sub_datas[2])

#--------------------测试乘法--------------------
class TestMul():
    def setup_class(self):
        print("------------测试乘法------------")

    @allure.story('乘法测试')
    @pytest.mark.run(order=3)
    def test_mul(self,get_mul_datas,fix_module):
        result = None
        try:
            result = fix_module.mul(get_mul_datas[0],get_mul_datas[1])
            if result == get_mul_datas[2]:
                print(f"{get_mul_datas[0]} * {get_mul_datas[1]}的计算结果是{result}，预期值是{get_mul_datas[2]},测试通过")
        except Exception as e:
            print(e)
        finally:
            with allure.step("乘法验证"):
                pytest.assume(result == get_mul_datas[2])


if __name__ == '__main__':
    pytest.main(["testcase.py"])