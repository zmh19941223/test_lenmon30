"""
======================
Author: 柠檬班-小简
Time: 2020/8/7 20:17
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
项目根目录下(最顶层)的conftest.py。跟day2包在同一级目录
整个项目下的，所有用例都可以共享

"""

import pytest

@pytest.fixture    # setup,teardown
def root():
    print(" 项目根目录下的conftest.py  作用域为测试函数的 **** 前置代码")
    yield True,100
    print(" 项目根目录下的conftest.py  作用域为测试函数的 **** 后置代码")