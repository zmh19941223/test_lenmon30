"""
======================
Author: 柠檬班-小简
Time: 2020/8/3 20:20
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest

pytestmark = pytest.mark.py30

@pytest.mark.smoke
def test_case1():
    print("case1")


# @pytest.mark.nmb
class TestABC:
    pytestmark = pytest.mark.nmb

    def test_abc2(self):
        print("用例1")
        assert 100 == 100

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_ccc(self):
        print("用例2")
        assert True

    def abc(self):
        print("AAAAAAA")

    # 测试重运行机制
    def test_fail(self):
        assert False