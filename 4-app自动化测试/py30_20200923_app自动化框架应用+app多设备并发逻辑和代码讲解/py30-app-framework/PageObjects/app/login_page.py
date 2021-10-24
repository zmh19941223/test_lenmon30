"""
======================
Author: 柠檬班-小简
Time: 2020/7/14 20:26
Project: java17-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
from PageLocators.app.loginPage_locator import LoginPageLocs as locs
from Common.basepage import Basepage

class LoginPage(Basepage):

    def login(self,username,passwd):
        self.input_text(locs.user_loc,username,"登陆页面_输入用户名")
        self.input_text(locs.passwd_loc, passwd, "登陆页面_输入密码")
        self.click_element(locs.loginButton_loc,"登陆页面_点击登陆按钮")

    def get_error_msg(self):
        pass