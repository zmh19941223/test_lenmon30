"""
======================
Author: 柠檬班-小简
Time: 2020/6/5 19:30
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
3.编写如下程序
优化去生鲜超市买橘子程序
a.收银员输入橘子的价格，单位：元／斤
b.收银员输入用户购买橘子的重量，单位：斤
c.计算并且 输出 付款金额
新需求：
d.使用捕获异常的方式，来处理用户输入无效数据的情况
"""

price = input('价格：')
weight = input('重量:')
try:
    float(price)
    float(weight)
except ValueError:
    print("输入的数据没法转成符点数！")
    # raise
else:
    count = float(price) * float(weight)  # 没有异常的情况下执行的。
    print(count)
