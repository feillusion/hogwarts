from time import sleep

import pytest
def test_01():
    print('start 1')
    sleep(6)
    print('end 1')
def test_02():
    print('start 2')
    sleep(3)
    print('end 2')

def test_03():
    print('start 2')
    sleep(5)
    print('end 3')

if __name__ == "__main__":
    pytest.main(["-s", "test_2.py",'--workers=1', '--tests-per-worker=2'])