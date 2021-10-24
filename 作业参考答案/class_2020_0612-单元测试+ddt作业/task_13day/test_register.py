import unittest

from task_13day.myddt import ddt, data
from task_13day.register import register

cases = [
    {"title": "注册成功", "data": ('python1', '123456', '123456'), "expected": {"code": 1, "msg": "注册成功"}},
    {"title": "注册失败-2次密码不一致", "data": ('python1', '1234567', '123456'), "expected": {"code": 0, "msg": "两次密码不一致"}},
    {"title": "注册失败-该账户已存在", "data": ('python26', '1234567', '123456'), "expected": {"code": 0, "msg": "该账户已存在"}},
    {"title": "注册失败-账号和密码必须在6-18位之间", "data": ('python21', '1234561234561234567', '1234561234561234567'),
     "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {"title": "注册失败-账号和密码必须在6-18位之间", "data": ('python1', '12345', '12345'), "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {"title": "注册失败-账号和密码必须在6-18位之间", "data": ('py01', '1234567', '1234567'), "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {"title": "注册失败-账号和密码必须在6-18位之间", "data": ('python1234561234567', '1234567', '1234567'), "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {"title": "注册失败-所有参数不能为空", "data": (None, '1234567', '1234567'), "expected": {'code': 0, 'msg': '所有参数不能为空'}},
    {"title": "注册失败-所有参数不能为空", "data": ('python678', None, None), "expected": {'code': 0, 'msg': '所有参数不能为空'}}
]


@ddt
class RegisterTestCase(unittest.TestCase):

    @data(*cases)
    def test_register(self, case):
        """正常注册"""
        # 第一步：准备用例的数据
        # 预期结果：expected     # 参数：data
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*case["data"])
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(case["expected"], res)
