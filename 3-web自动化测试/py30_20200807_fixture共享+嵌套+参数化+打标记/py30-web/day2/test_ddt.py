"""
======================
Author: 柠檬班-小简
Time: 2020/8/7 21:00
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest


@pytest.mark.parametrize("a", [(1, 3, 4), (10, 35, 45), (22.22, 22.22, 44.44)])
def test_add(a):
    print(a)


@pytest.mark.parametrize("a,b,c", [(1, 3, 4), (10, 35, 45), (22.22, 22.22, 44.44)])
def test_add2(a,b,c):
    print(a,b,c)

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(x,y)
