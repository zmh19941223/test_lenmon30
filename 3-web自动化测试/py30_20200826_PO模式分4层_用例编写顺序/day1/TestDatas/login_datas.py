"""
======================
Author: 柠檬班-小简
Time: 2020/8/26 20:53
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
# 登陆成功的测试数据
valid_user = ("18684720553","python")


# 登陆失败的数据 - 用户名为空/密码为空/用户格式不正确
invalid_data = [
        {"user":"","passwd":"python","check":"请输入手机号"},
        {"user": "18684720553", "passwd": "", "check": "请输入密码"},
        {"user": "1868472055", "passwd": "python", "check": "请输入手机号"},
        {"user": "186847205531", "passwd": "python", "check": "请输入手机号"}
    ]


