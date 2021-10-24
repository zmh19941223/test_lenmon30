"""
======================
Author: 柠檬班-小简
Time: 2020/7/14 20:28
Project: java17-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
from PageLocators.userPage_locator import UserPageLocs as locs
from Common.basepage import BasePage

class UserPage(BasePage):

    def click_avatar_to_login(self):
        """
        点击 我的柠檬  当中的个人头像，进入登陆页面。
        :return: 无
        """
        self.click_element(locs.login_avatar_loc,"用户页面_点击头像去登陆")

    def get_avatar_title(self):
        return self.get_ele_text(locs.login_avatar_loc,"用户页面_获取用户头像名字")