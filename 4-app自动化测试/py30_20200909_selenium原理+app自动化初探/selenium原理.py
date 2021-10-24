"""
======================
Author: 柠檬班-小简
Time: 2020/9/9 19:47
Project: py30-web-framework
Company: 湖南零檬信息技术有限公司
======================
"""
"""
http通信

客户端(代码)  - XXdriver(服务)  -   浏览器
语言selenium
指令(Command) - 接口
请求类型、请求url、请求数据


启动chromedriver程序
跟服务进行连接、建议一个会话。生成一个会话id
get: 发起一个http请求
find_elment: 发起另外一个http请求

https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com") # http请求

