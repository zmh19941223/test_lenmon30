"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:31
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest
from selenium import webdriver

# 定义fixture - 前置后置 - 作用域 - 返回值
@pytest.fixture
def init():
    # 实例化driver,访问登陆页面
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    yield driver
    driver.quit()
