"""
======================
Author: 柠檬班-小简
Time: 2020/9/18 19:34
Project: py30-app
Company: 湖南零檬信息技术有限公司
======================
"""
"""
混合应用：原生控件(xml) ＋　html
识别原生控件：app定位工具
html识别：浏览器的F12

打开手机上 开发者选项 - 边界布局。如果是原生控件，都会框起来。

android.webkit.WebView: 里面放的就是html

1、识别html
   并且你要从原生控件的操作，切换到html的操作。

2、开启webview的调试模式。
   http://testingpai.com/article/1595507219486

3、得到当前所有的contexts。   driver.contexts

4、切换：driver.switch_to.context。 一定会有NATIVE_APP, 可能还会有webview

================   html - web自动化    =================
5、元素识别工具：
   元素定位怎么看？ -- uc-devtools

6、驱动程序：chromedriver/安卓系统的webview版本
   版本怎么看？
   怎么得到手机的webview版本：
   1、工具：uc-devtools   https://dev.ucweb.com/docs/pwa/docs-zh/xy3whu
      进入到html里面，然后在包名后面的括号里，有webview的版本号。
   2、chrome浏览器里输入：chrome://inspect
   3、appium server的日志显示。
      [2020-09-18 09:03:44][Chromedriver] Webview version: 'Chrome/68.0.3440.70'
      
   在启动参数里，指定chromedriver获取路径：
   "chromedriverExecutableDir":"D:\ChromeDrivers\chrome67-69"

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


# 选择柠檬社区
loc = (MobileBy.ANDROID_UIAUTOMATOR,'text("柠檬社区")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))

# 获取所有的context
cons = driver.contexts
print("在进入混合页面之前，所有的上下文：",cons)

driver.find_element(*loc).click()

#　等待ｗｅｂｖｉｅｗ可见。
loc = (MobileBy.CLASS_NAME,'android.webkit.WebView')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
sleep(1)

# 获取所有的context
cons = driver.contexts
print("所有的上下文：",cons)

# # 切换
driver.switch_to.context('WEBVIEW_com.lemon.lemonban')

# ==========   html自动化    ========  chromedriver驱动程序是否与webview版本匹配？ ===========

loc = (MobileBy.XPATH, '//h2//a[contains(text(),"2020 最新柠檬班交友群来了！")]')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()