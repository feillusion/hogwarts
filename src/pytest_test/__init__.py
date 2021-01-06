#测试文件
#test_*.py
#*_test.py
#用例
#Test* 类包含的所有 test_*的方法（测试类不能带有__int__方法）
#不在class中的所有的 test_* 方法

#pytest也可以执行unittest框架写的用例和方法

#执行
#pytest 文件名.py
#pytest 文件名.py::类名
#pytest 文件名.py::类名::方法名
#-k 指定测试用例
#-v 打印详细运行日志信息
#-s 显示打印内容
#-x 一旦运行报错，就停止运行
#--maxfail=[num] 运行错误达到num时停止运行
#-m [标记名] 运行带有[标记名]的用例
#pytest --collect-only 只收集用例
#pytest --junitxml=./result.xml 生成执行结果文件
#pytest --setup-show 回溯fixture的执行过程



#setup、teardown  类方法开始、结束时执行
#setup_class、teardown_class  类开始、结束时执行
#setup_function、teardown_function  类外方法开始、结束时执行
#setup_module、teardown_module  模块开始、结束时执行
#setup_method、teardown_method


#pytest数据参数化
#@pytest.mark.parametrize(argnames,argvalues,ids)
#argnames:要参数化的变量，string(逗号分割),list,tuple
#argvalues：要参数化的值，list,list[tuple]
#ids:用例的别名，可不填
#eg.
# @pytest.mark.parametrize("a,b",[(10,20),(2,4)]，['失败','成功'])
# @pytest.mark.parametrize(["a","b"]],[(10,20),(2,4)])
# @pytest.mark.parametrize(("a","b")),[(10,20),(2,4)])
# def test_param(self,a,b):
#     print(a+b)
#参数化可以堆叠使用eg.
# @pytest.mark.parametrize("a",[1,2,3])
# @pytest.mark.parametrize("b",[1,2,3])
# def test_param(self,a,b):
#     print(a+b)


#加载yaml
# @pytest.mark.parametrize("a,b",yaml.safe_load(open(file_name)))
# def test_param(self,a,b):
#     print(a+b)


#pytest 配置文件
#同目录下创建  pytest.ini文件
#[pytest]
#markers=a b   自定义mark标签名
#addopts=a b   运行时参数（可添加多个，用空格隔开，所有参数与命令行一致）
#python_files 自定义测试文件命名规则
#python_class-Test_* 自定义测试类命名规则
#python_functions-test_* check_* 自定义测试方法命名规则
#testpaths - path1 path2
#norecursedir - dir1 dir2 运行时忽略某些文件夹