import allure
import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')

@allure.link("https://www.baidu.com/",name="link链接")
def test_link():
    assert 1 == 1

@allure.issue("https://www.baidu.com/","issue链接")
def test_issue():
    assert 1 == 1

@allure.testcase("https://www.baidu.com/","testcase链接")
@allure.description("这是一个描述")
def test_testcase():
    assert 1 == 1