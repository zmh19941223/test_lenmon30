"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""
import subprocess
import chardet


class ManageDevices:
    """
       1、重启adb服务。
       2、通过adb devices命令获取当前平台中,已连接的设备个数，和设备uuid.
       3、通过adb -P 5037 -s 设备uuid shell getprop ro.build.version.release获取每一个设备的版本号。
       4、将所有已连接设备的设备名称、设备版本号存储在一个列表当中。
       5、通过调用get_devices_info函数，即可获得4中的列表。
    """

    def __init__(self):
        self.__devices_info = []
        # 重启adb服务
        self.__run_command_and_get_stout("adb kill-server")
        self.__run_command_and_get_stout("adb start-server")

    def get_devices_info(self):
        """
        获取已连接设备的uuid,和版本号。
        :return: 所有已连接设备的uuid,和版本号。
        """
        self.__get_devices_uuid()
        print(self.__devices_info)
        self.__get_device_platform_vesion()
        return self.__devices_info

    def __get_devices_uuid(self):
        """
        获取已连接的所有设备的设备uuid
        :return: 列表。所有设备的uuid
        """
        # 终端命令行命令。
        command = "adb devices"
        result = self.__run_command_and_get_stout(command)
        device_list = result.split("\n")
        print("adb结果 ：")
        print(device_list)
        for item in device_list:  # 遍历adb devices 输出的内容
            if item.find("\t") != -1:  # 获取设备信息
                temp = item.split("\t")
                if temp[1] == "device":  # 设备为可识别状态。有些可能是offline、unauthorized等。
                    new_device = {"deviceName": temp[0]}
                    self.__devices_info.append(new_device)

    def __get_device_platform_vesion(self):
        """
        获取已连接设备的安卓版本号。
        """
        if self.__devices_info:
            for dev in self.__devices_info:
                command = "adb -P 5037 -s {} shell getprop ro.build.version.release".format(dev["deviceName"])
                print(command)
                s = self.__run_command_and_get_stout(command)
                dev["platformVersion"] = s

    @staticmethod
    def __run_command_and_get_stout(command):
        """
        执行终端命令行并获取返回值。
        :param command: 命令
        :return: 执行结果
        """
        # 执行command的，并获取命令执行之后的输出数据。
        stdout, stderror = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True).communicate()
        # 编码处理
        if stdout:
            encoding = chardet.detect(stdout)["encoding"]
            result = stdout.decode(encoding)
            result = result.strip("\r\n")   # 去掉首尾的换行回车
            return result


if __name__ == '__main__':
    md = ManageDevices()
    devices_info = md.get_devices_info()
    print(devices_info)
