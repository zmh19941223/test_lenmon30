"""
======================
Author: 柠檬班-小简
Time: 2020/9/23 20:34
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 在andriod 7.1.2 上面打开柠檬班app
desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "huawei",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True,
    "chromedriverExecutableDir":"D:\ChromeDrivers\chrome67-69"
}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


# 点击我的题库
loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_tiku")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击题库类别
loc = (MobileBy.ANDROID_UIAUTOMATOR,'text("MySQL数据库")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 退出到主页
driver.start_activity("com.lemon.lemonban","com.lemon.lemonban.activity.MainActivity")