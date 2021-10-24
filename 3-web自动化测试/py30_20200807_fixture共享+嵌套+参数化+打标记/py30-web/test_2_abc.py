"""
======================
Author: 柠檬班-小简
Time: 2020/8/3 20:20
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest

@pytest.mark.smoke
def test_case1():
    print("case1")



class TestABC:

    def test_abc2(self):
        print("用例1")
        assert 100 == 100

    @pytest.mark.demo
    def test_ccc(self):
        print("用例2")
        assert True

    def abc(self):
        print("AAAAAAA")