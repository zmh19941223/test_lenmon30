"""
======================
Author: 柠檬班-小简
Time: 2020/9/11 21:20
Project: py30-app
Company: 湖南零檬信息技术有限公司
======================
"""
"""
adb启停，默认端口5037
adb kill-server
adb start-server

adb devices: 

adb install apk包
adb unintall 应用包名


获取当前打开的页面：
adb shell dumpsys activity | find "mResumedActivity"
adb shell dumpsys activity activities | findstr mResumedActivity

"""