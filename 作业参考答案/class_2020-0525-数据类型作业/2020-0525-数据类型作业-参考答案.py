"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""

"""
1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
（提示：通过字符串分割，拼接，列表反序等知识点来实现）
"""
str1 = "hello xiao mi"
# 按空格分割
list1 = str1.split(" ")
# 列表反序
list1.reverse()
# 再次拼接为字符串
str_new = " ".join(list1)
print(str_new)   # 结果为：mi xiao hello


"""
2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
        3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
        4、平台为了保护你的隐私，需要你删除你的联系方式；
        5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
"""
# 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来
name = input("请输入你的姓名：")
sex = input("请输入你的性别：")
age = input("请输入你的年龄：")
my_info = {"name": name, "sex": sex, "age": age}
# 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(my_info["name"],my_info["age"],my_info["sex"]))
# 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
my_info["height"] = 180
my_info["contact"] = "18600110011"
# 4、平台为了保护你的隐私，需要你删除你的联系方式；
del my_info["contact"]
# 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
my_info["best"] = "写python"
print(my_info)


"""
3、利用下划线将列表li=[“python”,“java”,“php”]的元素拼接成一个字符串，然后将所有字母转换为大写，
"""
li = ["python", "java", "php"]
# 用下划线拼成一个字符串
lan_str = "_".join(li)
upper_str = lan_str.upper()
print(upper_str)


"""
4、利用切片把 'http://www.python.org'中的python字符串取出来
"""
address = 'http://www.python.org'
temp = address.split(".")   # ['http://www', 'python', 'org']
print(temp[1])

"""
有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}
"""
t1 = ("aa", 11)
t2 = ("bb", 22)
li1 = [("cc", 11)]

dict1 = {t1[0]: t1[1], li1[0][0]: li1[0][1], t2[0]: t2[1]}
print(dict1)
