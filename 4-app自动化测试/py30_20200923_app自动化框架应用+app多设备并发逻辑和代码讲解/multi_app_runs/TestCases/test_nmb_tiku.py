#!/usr/bin/python3
"""
@File    : test_nmb_tiku.py
@Time    : 2019/8/16 15:08
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
import pytest
from TestCases.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

@pytest.mark.usefixtures("start_app")
def test_click_tiku(start_app):
    bp = BasePage(start_app)
    bp.click_element(("id","com.lemon.lemonban:id/navigation_tiku"),"首页_点击题库")
    print("点击！！")
    bp.click_element((MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Python自动化\")"),"题库页面_点击python自动化")



