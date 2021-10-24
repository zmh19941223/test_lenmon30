#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: conftest
# Author: liyuan
# Time: 11:35
import pytest
from appium import webdriver

# 设置pytest支持参数: --cmdopt
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="{platformName:'Android',platformVersion:'5.1.1'}", help="my devices info"
    )

# 获取--cmdopt命令行参数的值。
@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")



@pytest.fixture
def start_app(cmdopt):
    device = eval(cmdopt)
    print("开始与设备 {} 进行会话，并执行测试用例 ！！".format(device["caps"]["deviceName"]))
    driver = start_appium_session(device)
    yield driver
    driver.close_app()
    driver.quit()


# 与appium建议连接，启动与appium的会话
def start_appium_session(device,server_params=None):
    # 其它的启动参数
    if server_params is not None:
        device["caps"].update(server_params)
    # 启动会话
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(device["port"]),device["caps"])
    print("启动与设备  {}  会话成功！appium server端口为：{}".format(device["caps"]["deviceName"],device["port"]))
    return driver