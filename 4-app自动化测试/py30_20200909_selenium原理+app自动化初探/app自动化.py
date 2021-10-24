"""
======================
Author: 柠檬班-小简
Time: 2020/9/9 20:39
Project: py30-web-framework
Company: 湖南零檬信息技术有限公司
======================
"""

"""
客户端(代码)(windows)  -     appium server(服务)(windows)                -   真机/模拟器(android/ios)
各种语言appium
指令(Command) - 接口
请求类型、请求url、请求数据

appium server(服务)(windows)  -     真机/模拟器(android/ios)
  发送请求(客户端)                         接收请求(服务端)
                                appium在设备上安装软件 - 用来接收请求(端口号)
                                  自带自动化框架 - 
                                


客户端(代码)(windows)  -    appium server(服务)(windows)    -   真机/模拟器(android/ios)    
                                                         ADT
appium server:
1、命令行版本
2、桌面版：appium-desktop       
"""
# adb devcies  获取已连接的设备     真机：开启 - 开发者模式 - usb调试模式


# 在andriod 7.1.2 上面打开柠檬班app
#　包名 appPackage
# 入口activity
# 命令语法：
# aapt dump badging apk应用名(路径不能有中文)
# package: name='com.lemon.lemonban'
# launchable-activity: name='com.lemon.lemonban.activity.WelcomeActivity'  label='' icon=''

from appium import webdriver

# 在andriod 7.1.2 上面打开柠檬班app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "huawei",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True

}

# 跟appium建立连接，然后再把启动参数发过去。
webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 执行时，请保证：1 设备在线  2、appium server已启动


