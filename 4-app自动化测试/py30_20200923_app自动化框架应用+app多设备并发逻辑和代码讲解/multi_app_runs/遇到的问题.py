"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""
"""
2个及2个以上设备并发时，会有一个设备出现socket hang up
通过日志查看，appium在代理操作时，用的都是8200端口
多个appium server都用8200端口就会出现问题

那么8200是啥端口呢

adb -P 5037 -s 08e7c5997d2a forward tcp\:8200 tcp\:6790
将本地8200端口的数据，转发到安卓设备的6790端口
本地启动多个appium server，都是用的8200端口，就会出现冲突。
应该设置为，每一个appium server用不同的端口号。
启动参数当中：systemPort=8200 
每个设备都换不同的端口

"""