"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

appium_logs_dir = os.path.join(base_dir, "Outputs", "appium_server_logs")

reports_dir = os.path.join(base_dir, "Outputs", "test_reports")
