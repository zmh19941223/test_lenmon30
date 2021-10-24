"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""
"""
第一步：从设备池当中，获取当前连接的设备。若设备池为空，则无设备连接。

第二步：若设备池不为空，启动一个进程，用来启动appium server.与设备个数对应。起始server端口为4723，每多一个设备，端口号默认+4

第三步：若设备池不为空，则用线程，来执行app自动化测试。
"""
from concurrent.futures import ThreadPoolExecutor,as_completed
import time
import pytest
import platform
import os

from Common.manger_devices_pool import devices_pool
from Common.manager_appium_server import ManageAppiumServer
from Common.handle_path import reports_dir

# 获取代码所在平台
appium_server_path = ""
platform_name = ""

plat = platform.platform()
if plat.find("Darwin") != -1:
    platform_name = "MAC"
    appium_server_path = '/Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js'
elif plat.find("Windows") != -1:
    platform_name = "WIN"
    appium_server_path = r'C:\Program Files\Appium\resources\app\node_modules\appium\build\main.js'


# 运行测试用例的函数
def run_cases(device):
    print(["-s", "-v", "--cmdopt={}".format(device)])
    reports_path = os.path.join(reports_dir,"test_result_{}_{}.html".format(device["caps"]["deviceName"], device["port"]))
    pytest.main(["-s", "-v",
                 "--cmdopt={}".format(device),
                 "--html={}".format(reports_path)]
                )


if __name__ == '__main__':

    # 第一步：从设备池当中，获取当前连接的设备的启动信息和appium端口。若设备池为空，则无设备连接。
    devices = devices_pool()

    # 第二步：若设备池不为空，启动appium server.与设备个数对应。起始server端口为4723，每多一个设备，端口号默认+4
    if devices and platform_name and appium_server_path:
        # 创建线程池
        T = ThreadPoolExecutor()
        # 实例化appium服务管理类。
        mas = ManageAppiumServer(appium_server_path)
        for device in devices:
            # kill 端口，以免占用
            mas.stop_appium(platform_name,device["port"])
            # 启动appium server
            task = T.submit(mas.start_appium_server,device["port"])
            time.sleep(1)

        # 第三步：若设备池不为空，在appium server启动的情况下，执行app自动化测试。
        time.sleep(15)
        obj_list = []
        for device in devices:
            index = devices.index(device)
            task = T.submit(run_cases,device)
            obj_list.append(task)
            time.sleep(1)

        # 等待自动化任务执行完成
        for future in as_completed(obj_list):
            data = future.result()
            print(f"sub_thread: {data}")

        # kill 掉appium server服务,释放端口。
        for device in devices:
            ManageAppiumServer.stop_appium(platform_name, device["port"])





