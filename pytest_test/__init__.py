#测试文件
#test_*.py
#*_test.py
#用例
#Test* 类包含的所有 test_*的方法（测试类不能带有__int__方法）
#不在class中的所有的 test_* 方法

#pytest也可以执行unittest框架写的用例和方法

#执行
#pytest
#-k 指定测试用例
#-v 匹配包含名字的用例

#pytest数据参数化
#@pytest.mark.parametrize(argnames,argvalues)
#argnames:要参数化的变量，string(逗号分割),list,tuple
#argvalues：要参数化的值，list,list[tuple]
#eg.
# @pytest.mark.parametrize("a,b",[(10,20),(2,4)])
# @pytest.mark.parametrize(["a","b"]],[(10,20),(2,4)])
# @pytest.mark.parametrize(("a","b")),[(10,20),(2,4)])
# def test_param(self,a,b):
#     print(a+b)

#加载yaml
# @pytest.mark.parametrize("a,b",yaml.safe_load(open(file_name)))
# def test_param(self,a,b):
#     print(a+b)