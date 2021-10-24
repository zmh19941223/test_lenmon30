"""
======================
Author: 柠檬班-小简
Time: 2020/9/14 20:51
Project: py30-app
Company: 湖南零檬信息技术有限公司
======================
"""
"""
id 
class_name
accessibility_id    (description)

android_uiautomator  (UiAutomator2)
xpath


坐标

UiAutomator - UiSelector类完成的  java语言-字符串必须是双引号
#  new UiSelector().resourceId("")  # appium 1.15之前
#  resourceId("")   # appium 1.15之后

# 多属性组合 
resourceId("").text("") 
"""



from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 在andriod 7.1.2 上面打开柠檬班app
desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "huawei",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True

}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# loc = (MobileBy.ID,"com.lemon.lemonban:id/navigation_tiku")
# WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
# driver.find_element(MobileBy.ID,"com.lemon.lemonban:id/navigation_tiku").click()

# android_uiautomator  -- UiAutomator2- UiSelector
loc = (MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.lemon.lemonban:id/navigation_tiku")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 选择题库类型
loc = (MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.lemon.lemonban:id/fragment_category_type").text("MySQL数据库")')
# xpath定位
# loc = (MobileBy.XPATH,'//android.widget.TextView[@text="MySQL数据库"]')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


# accessibility_id定位
# driver.find_element_by_accessibility_id()



from time import sleep

sleep(5)
driver.quit()

# 滑动  触屏操作  多点触控
# h5混合应用 - 微信小程序/公众号
# toast