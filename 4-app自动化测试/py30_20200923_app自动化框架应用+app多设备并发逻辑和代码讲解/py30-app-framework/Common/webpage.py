"""
======================
Author: 柠檬班-小简
Time: 2020/9/21 20:36
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import os
import time

from Common.my_logger import logger
from Common.handle_path import screenshot_dir

class WebPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_window(self,name="new"):
        # 等待一下
        time.sleep(1)
        # 获取所有的句柄
        wins = self.driver.window_handles
        if name == "new":
            self.driver.switch_to.window(wins[-1])

    # js的值来修改value值。 -- 固定流程，你都是可以封装。
    # driver.find_element()来找到元素。传到js里面，arguments[0].value=new_value

    def back_last_page(self):
        logger.info("回退到上一页")
        self.driver.back()
        return self

    def refresh_page(self):
        logger.info("刷新当前页面")
        self.driver.refresh()
        return self
