"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:01
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
"""
前置
测试数据：18684720553  python

"""

import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage

@pytest.mark.usefixtures("init")
class TestLogin:

    def test_login_success(self,init):
        # 登陆 - 步骤
        LoginPage(init).login("18684720553","python")
        # 断言 -
        assert HomePage(init).is_exit_exist()
