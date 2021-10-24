"""
======================
Author: 柠檬班-小简
Time: 2020/9/16 20:06
Project: py30-app
Company: 湖南零檬信息技术有限公司
======================
"""
"""
TouchAction: 操作 + 执行(perform)
操作 - 有3个参数：元素对象、x、y (二选一)
tap：点击
press：按住
long_press：长按住
wait: 等待
move_to:移动
release：释放


执行：perform


设备的大小：driver.get_window_size()
"""

from appium.webdriver.common.touch_action import TouchAction
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
    "noReset":True

}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 切换到题 库
loc = (MobileBy.ID,'com.lemon.lemonban:id/navigation_tiku')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 等待题 库页面元素加载
loc = (MobileBy.ID,'com.lemon.lemonban:id/fragment_category_type')
WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located(loc))
sleep(0.5)


# 滑屏操作
# 设备大小
size = driver.get_window_size()
# size
x = size["width"] * 0.5
y_start = size["height"] * 0.9
y_end = size["height"] * 0.1

# ta = TouchAction(driver)  # 实例化
# ta.press(x=x,y=y_start).wait(200).move_to(x=x,y=y_end).release()  # 触屏动作
# ta.perform()  # 执行触屏操作

driver.swipe(x,y_start,x,y_end,200)

sleep(7)
driver.quit()
