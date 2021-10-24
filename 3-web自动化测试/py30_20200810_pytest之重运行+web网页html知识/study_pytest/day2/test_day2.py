"""
======================
Author: 柠檬班-小简
Time: 2020/8/5 21:19
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest

# @pytest.fixture    # setup,teardown
# def init(init2):
#     print(" 作用域为测试函数的 **** 前置代码")
#     yield True,100
#     print(" 作用域为测试函数的 **** 后置代码")


import pytest

# @pytest.mark.usefixtures("init")   # 执行函数名叫做init的前置后置fixture
def test_abc(init2):  # 参数init = 函数名叫做init的返回值
    print("=== 函数用例 ====")
    print("fixture的返回值为：",init2)


# @pytest.mark.usefixtures("class_fix")  # 整个TestDay测试类，只执行一次。
# @pytest.mark.usefixtures("init")   # 这个类下面的所有测试用例，都会执行前置后置
# class TestDay:
#
#     # @pytest.mark.usefixtures("init")
#     def test_new(self,init):
#         print(" === 类下的用例1 ===")
#
#     def test_new2(self):
#         print(" === 类下的用例2 ===")
#
#     # @pytest.mark.usefixtures("init")
#     def test_new3(self):
#         print(" === 类下的用例3 ===")