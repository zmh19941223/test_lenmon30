"""
======================
Author: 柠檬班-小简
Time: 2020/5/18 20:28
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
# 注释：说明。
# #代表单行注释  ctrl + /
# 多行注释   三引号(双引号，单引号)  符号都是英文状态
"""
今天是30期第一次课
我是第一次使用多行注释
我好开心
我开始学代码了
"""

'''
1111
2222
333
开始掉头发了
'''

# 每一行只做一件事情。
# print输出功能：输出hello world
# 要求：输出5次hello world!
# 只想改一次，然后所有用到我的都同时更新！！
# 变量名(标识符) = 值/数据(数据类型)
# 变量名: 见名知义。一定可读性
today = "hello,nmb,py30,xj!"
# 使用
py30 = "good"
hello_world = "hello,world!"

print(today)   # ctrl + B查看源码。
print(today)
print(today)
print(today)
print(today)

# 字符串：数据类型。 双引号/单引号括起来。

# 查看关键字
# import keyword
# print(keyword.kwlist)

age = 18.5
age_str = "18.5"
age_str2 = '18.5'
person_info = "你好，我叫XXx，我来自XXX,我现在工作" \
              "是XXx，我的项目是XXX,我负责的XXX"

# 三引号 - 多行字符串
person_info2 = """
你好，我叫XXx
我来自XXX,我现在工作XXX
我的项目是XXX,我负责的XXX
我现在的技能是。。。
"""

is_ten_oclock = False
after_ten = True

# 获取数据类型
print(type(age))
print(type(age_str))

# print(age)
# print(person_info)
# print(person_info2)

