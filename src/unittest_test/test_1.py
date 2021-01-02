import unittest
import HTMLTestRunner_PY3

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("---类开始---\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("---类结束---")

    def setUp(self) -> None:
        print("---用例开始---")

    def tearDown(self) -> None:
        print("---用例结束---\n")


    def test_1(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        print("case1")

    #@unittest.skip("本次不执行")
    def test_2(self):
        #self.assertTrue('FOO'.isupper())
        #self.assertFalse('Foo'.isupper())
        print("case2")

    def test_3(self):
        # s = 'hello world'
        # self.assertEqual(s.split(), ['hello', 'world'])
        # # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)
        print("case3")

    def test_4(self):
        # self.assertTrue('HAHA'.isupper())
        print("case4")

class TestCases1(unittest.TestCase):

    def test_01(self):
        print("这是另一个类中的函数")



if __name__ == '__main__':
    #执行全部用例
    #unittest.main()

    #添加指定的用例
    # suite = unittest.TestSuite()
    # suite.addTest(TestCases('test_3'))
    # suite.addTest(TestCases('test_2'))
    #添加指定类
    # suite=unittest.TestLoader().loadTestsFromTestCase(TestCases)
    #指定路径(可以写在别的py文件里)
    test_dir = ""
    suite = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
    #执行添加的用例/类
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #执行添加的用例/类，并生成报告
    with open("result.html", "wb") as report:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=report, title="tesc_report", description="test_description")
        runner.run(suite)