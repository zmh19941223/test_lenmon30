"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""
import yaml
import os

from Common.handle_path import base_dir
from Common.manager_devices_info import ManageDevices

"""
设备启动参数管理池。
每一个设备：对应一个启动参数，以及appium服务的端口号。

1、desired_caps_config/desired_caps.yaml文件中存储了启动参数模板。
2、从1中的模板读取出启动参数。
3、从设备列表当中，获取每个设备的设备uuid、版本号，与2中的启动参数合并。
4、每一个设备，指定一个appium服务端口号。从4723开始，每多一个设备，默认递增4
5、每一个设备，指定一个本地与设备tcp通信的端口号。从8200开始，每多一个设备，默认递增4.
   在启动参数当中，通过systemPort指定。
   因为appium服务会指定一个本地端口号，将数据转发到安卓设备上。
   默认都是使用8200端口，当有多个appium服务时就会出现端口冲突。会导致运行过程中出现socket hang up的报错。
"""

__all__ = ["devices_pool"]


def devices_pool(port=4723,system_port=8200):
    """
    设备启动参数管理池。含启动参数和对应的端口号
    :param port: appium服务的端口号。每一个设备对应一个。
    :param system_port: appium服务指定的本地端口，用来转发数据给安卓设备。每一个设备对应一个。
    :return: 所有已连接设备的启动参数和appium端口号。
    """
    desired_template = __get_yaml_data()
    devs_pool = []
    # 获取当前连接的所有设备信息
    m = ManageDevices()
    all_devices_info = m.get_devices_info()
    # 补充每一个设备的启动信息，以及配置对应的appium server端口号
    if all_devices_info:
        for dev_info in all_devices_info:
            dev_info.update(desired_template)
            dev_info["systemPort"] = system_port
            new_dict = {
                "caps": dev_info,
                "port": port
            }
            devs_pool.append(new_dict)
            port += 4
            system_port += 4
    return devs_pool


def __get_yaml_data():
    """
    从yaml中读取默认的启动参数
    """
    yaml_path = os.path.join(base_dir,"desired_caps_config","desired_caps.yaml")
    with open(yaml_path,encoding="utf-8") as fs:
        desired_template = yaml.load(fs,yaml.FullLoader)
        return desired_template


if __name__ == '__main__':
    print(devices_pool())


