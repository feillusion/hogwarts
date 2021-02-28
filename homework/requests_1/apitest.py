import requests


class TestContact:
    def setup_class(self):
        #获取access_token
        self.corpid = 'ww51bb78344d7cccdf'
        self.contact_secret = '_9UzNkQk_8WxwWGkK-eSKo4xz1m8xwKAkx8rniYURH8'
        self.token = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
                                  f"corpid={self.corpid}&corpsecret={self.contact_secret}").json()['access_token']
        print('class start')

    def teardown_class(self):
        print('class end')

    def test_create(self):
        data = {
            "userid": "demo",
            "name": "demo1",
            "mobile": "+86 13800000000",
            "department": [1]
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',
                          json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'created'

    def test_update(self):
        data = {
            "userid": "demo",
            "name": "demo2"
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}',
                          json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'updated'

    def test_get(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=demo')
        print(r.json())
        assert r.json()['errmsg'] == 'ok'
        assert r.json()['userid'] == 'demo'
        assert r.json()['name'] == 'demo2'

    def test_delete(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=demo')
        print(r.json())
        assert r.json()['errmsg'] == 'deleted'