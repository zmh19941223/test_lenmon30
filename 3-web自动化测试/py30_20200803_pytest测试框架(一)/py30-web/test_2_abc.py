"""
======================
Author: 柠檬班-小简
Time: 2020/8/3 20:20
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""

# def setup_module():
#     print(" 前置 -- 模块级别 -- ")
#
# def teardown_module():
#     print(" 后置 *** 模块级别 *** ")


# def setup():
#     print(" 用例--前置--")
#
def test_case1():
    print("case1")
#
# def test_case2():
#     print("case2")


class TestABC:

    # def setup(self):
    #     print(" 用例--前置--")
    #
    # def teardown(self):
    #     print(" 用例 *** 后置 ***")

    # @classmethod
    # def setup_class(cls):
    #     print(" 类 -- 前置 --")
    #
    # @classmethod
    # def teardown_class(cls):
    #     print("类 ** 后置 **")

    def test_abc2(self):
        print("用例1")
        assert 100 == 100

    def test_ccc(self):
        print("用例2")
        assert True

    def abc(self):
        print("AAAAAAA")