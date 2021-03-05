import pytest
import yaml
from homework.requests_2.qiyeweixin_api.contact import Contact


class TestContact(Contact):
    #执行该类下测试用例前执行，创建实例并打印开始
    def setup_class(self):
        self.test = Contact().token()
        print('通讯录测试开始')
    #执行该类下测试用例后执行，并打印结束
    def teardown_class(self):
        print('通讯录测试结束')

    #测试创建成员接口
    @pytest.mark.parametrize('data,asserts',yaml.safe_load(open('qiyeweixin.yaml','r',encoding='utf-8'))['createmember'])
    def test_create_member(self,data:dict,asserts:dict):
        r = self.test.create_member(data)
        print(r)
        for i in asserts.keys():
            assert asserts[i] in r[i]

    #测试更新成员接口
    @pytest.mark.parametrize('data,asserts',yaml.safe_load(open('qiyeweixin.yaml','r',encoding='utf-8'))['updatemember'])
    def test_update_member(self,data:dict,asserts:dict):
        r = self.test.update_member(data)
        print(r)
        for i in asserts.keys():
            assert asserts[i] in r[i]

    #测试获取成员信息接口
    @pytest.mark.parametrize('userid,asserts',yaml.safe_load(open('qiyeweixin.yaml','r',encoding='utf-8'))['getmember'])
    def test_get_member(self,userid:str,asserts:dict):
        r = self.test.get_member(userid)
        print(r)
        for i in asserts.keys():
            assert asserts[i] in r[i]

    #测试删除成员接口
    @pytest.mark.parametrize('userid,asserts',yaml.safe_load(open('qiyeweixin.yaml','r',encoding='utf-8'))['deletemember'])
    def test_delete_member(self,userid:str,asserts:dict):
        r = self.test.delete_member(userid)
        print(r)
        for i in asserts.keys():
            assert asserts[i] in r[i]

if __name__ == '__main__':
    pytest.main(['qiyeweixin.py'])