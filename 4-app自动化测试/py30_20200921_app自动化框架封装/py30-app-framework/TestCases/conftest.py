"""
======================
Author: 柠檬班-小简
Time: 2020/9/21 21:38
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
import yaml
from Common.handle_path import conf_dir
import os
from appium import webdriver
import pytest


# 前置是什么  步骤是什么，涉及哪些页面的哪些操作，断言是什么，怎么用代码去表达？
# 1、启动会话，2、登陆成功
@pytest.fixture
def init_driver():
    # 启动会话
    driver = _basedriver()
    # 登陆成功 - 判断一下是否登陆了？
    _deal_login(driver)
    yield driver
    driver.quit()



def _basedriver(port=4723,**kwargs):
    # 读取yaml启动参数
    fs = open(os.path.join(conf_dir,"desired_caps.yaml"),encoding="utf-8")
    desired_caps = yaml.load(fs,Loader=yaml.FullLoader)
    # if kwargs:
    #     for key,value in kwargs.items():
    #         desired_caps[key] = value
    # 启动会话 - 实例化driver对象
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port),desired_caps)
    # 返回driver对象
    return driver


def _deal_login(driver):
    # 点击题库，查看页面是否有  去登录 元素
    # 如果没有，pass
    # 如果有，调用页面登陆行为。
    try:
        # 等待元素可见 - 去登陆这个元素 - 等5s
        pass
    except:
        pass # 已登陆，啥也不用干
    else:
        # 调用页面登陆行为。-- 自己实现
        pass
