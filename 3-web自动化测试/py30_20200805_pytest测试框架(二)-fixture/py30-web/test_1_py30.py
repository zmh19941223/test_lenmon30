"""
======================
Author: 柠檬班-小简
Time: 2020/8/3 21:00
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
def add(*args):
    sum = 0
    if args:
        for item in args:
            sum += item
    return sum


def test_sum():
    assert add(1,1) == 2

def test_add1():
    assert 300 == add(100,200)

def test_add2():
    assert 300 == add(10,50,230)

