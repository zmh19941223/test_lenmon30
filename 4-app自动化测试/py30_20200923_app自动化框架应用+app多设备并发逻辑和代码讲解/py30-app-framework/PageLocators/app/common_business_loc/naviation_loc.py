"""
======================
Author: 柠檬班-小简
Time: 2020/9/21 21:55
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""

from appium.webdriver.common.mobileby import MobileBy as MB

class NavigationLoc:
        # 导航栏
        # 主页
        home_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_home")
        # 题库
        tiku_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_tiku")
        # 我的柠檬
        my_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_my")