import pytest
import requests

from src.platform_test.backend import db


def test_db():
    db.create_all()

def test_get():
    r = requests.get('http://127.0.0.1:5000/testcase')
    assert r.status_code == 200

def test_post():
    datas={
        'name':'test3',
        'steps':[
            'diyibu',
            'dierbu'
        ],
        'expect':'expect3'
    }
    r = requests.post('http://127.0.0.1:5000/testcase',json=datas)
    assert r.status_code == 200