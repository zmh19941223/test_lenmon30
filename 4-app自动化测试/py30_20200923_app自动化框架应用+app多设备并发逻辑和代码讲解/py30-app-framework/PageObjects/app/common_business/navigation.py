"""
======================
Author: 柠檬班-小简
Time: 2020/9/21 21:53
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
from Common.apppage import AppPage

from Common.basepage import Basepage
from PageLocators.app.common_business_loc.naviation_loc import NavigationLoc as locs

class Navigation(Basepage):

    def switch_nav_by_name(self,name):
        if name == "主页":
            self.click_element(locs.home_nav_loc,"导航栏_切换到主页")
        elif name == "题库":
            self.click_element(locs.tiku_nav_loc, "导航栏_切换到题库")
        elif name == "我的柠檬":
            self.click_element(locs.my_nav_loc, "导航栏_切换到我的柠檬")