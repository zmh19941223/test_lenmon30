"""
======================
Author: 柠檬班-小简
Time: 2020/9/21 20:36
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
from appium.webdriver.webdriver import WebDriver
from Common.basepage import Basepage
from time import sleep

from Common.my_logger import logger

class AppPage(Basepage):

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 获取设备大小
    def get_device_size(self):
        size = self.driver.get_window_size()
        return size["width"], size["height"]
        # try:
        #     size = self.driver.get_window_size()
        # except:
        #     self.get_page_img()
        # else:
        #     return size["width"],size["height"]


    # 根据方向来滑动屏幕。80%
    def swipe_by_direction(self,direction):
        width,height = self.get_device_size()

        if direction == "up" or direction == "down":
            start_x = width * 0.5
            end_x = width * 0.5
            if direction == "up":  # 向上滑动
                start_y = height * 0.9
                end_y = height * 0.1
            else:  # 向下滑动
                start_y = height * 0.1
                end_y = height * 0.9
        else:
            pass

        try:
            self.driver.swipe(start_x,start_y,end_x,end_y,200)
        except:
            pass

    # toast处理  xpath - 等待存在
    def get_toast_msg(self,toast_value,page_action):
        loc = ("xpath",'//*[contains(@text,"{}")]'.format(toast_value))
        try:
            self.wait_page_contains_element(loc,page_action,10,0.01)
        except:
            pass

    # 混合应用 - h5
    # 识别-开调试-获取所有的contexts-切换到webview contexts里-html自动化
    def switch_to_webview(self,webview_name):
        cons = self.driver.contexts
        if webview_name in cons:
            self.driver.switch_to.context(webview_name)
            sleep(1)
        else:
            pass  # 提示一下，webview没有获取到。

    # 微信小程序
    # 识别-开调试-获取小程序所在的进程名称
    # 启动参数配置-微信操作进入小程序页面当中-切换操作-获取所有的窗口-进入到小程序所在的窗口




