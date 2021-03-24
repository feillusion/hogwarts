import requests

from homework.backend.backend import db


def test_db():
    db.create_all()


class TestTestcaseservice:
    def test_get(self):
        r = requests.get('http://127.0.0.1:5000/testcase?name=test1')
        assert r.status_code == 200
        print(r.json())

    def test_post(self):
        datas={
            'name':'',
            'steps':[
                'step1',
                'step2',
                'step3'
            ],
            'expect':'expect132'
        }
        r = requests.post('http://127.0.0.1:5000/testcase',json=datas)
        print(r.json())
        assert r.status_code == 200

    def test_delete(self):
        datas={
            'id': 8
        }
        r = requests.delete('http://127.0.0.1:5000/testcase',json=datas)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        datas={
            'id' : '5',
            'name':'test13',
            'steps':[
                'step11',
                'step22',
                'step33'
            ],
            'expect':'expect13'
        }
        r = requests.put('http://127.0.0.1:5000/testcase',json=datas)
        print(r.json())
        assert r.status_code == 200

class TestTask:
    def test_post(self):
        datas = {
            'name':'task132',
            'casesid':[2,6,7],
            'description':'description2'
        }
        r =  requests.post('http://127.0.0.1:5000/task',json=datas)
        print(r.json())
        assert r.status_code == 200

    def test_get(self):
        r= requests.get('http://127.0.0.1:5000/task')
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        datas = {
            'id':'1',
            'name':'task123',
            'casesid':[1],
            'description':'description'
        }
        r =  requests.put('http://127.0.0.1:5000/task',json=datas)
        print(r.json())
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete('http://127.0.0.1:5000/task?id=2')
        print(r.json())
        assert r.status_code == 200