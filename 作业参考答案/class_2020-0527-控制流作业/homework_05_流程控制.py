import random


"""
1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或
20%）和最终价格。

"""
#
# price = int(input("金额："))
# # 类型是什么？？？
# price_after = price
#
# # if (price >= 50) and (price <= 100):
# # if 50 < price > 100:
# if  50 <= price <= 100:
#     # 打折以后的价格 Decimal
#     price_after =  price * (1- 0.1)
# elif price > 100 :
#     price_after = price * (1 - 0.2 )
#
# print(price_after) # 没有定义




"""
判断是否为闰年

提示:

    输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）

    如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”

什么是闰年，请自行了解（需求文档没有解释）

"""

# year = int(input("输入年份") )
# if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 ):
#     print('这是一个闰年')
# else:
#     print('不是一个软年')





"""
求三个整数中的最大值

提示：三个整数使用input提示用户输入
"""
# a = int(input("第一个数"))
# b = int(input("第二个数"))
# c = int(input("第三个数"))

# a = 10
# b = 20
# c = 30
#
# # max(a, b, c)
#
# #
# max_num = a
# if a < b:
#     max_num = b
#
# if max_num < c:
#     max_num = c
# print(max_num)

# 扩展方法
# a = 4
# b = 7
# c = 9
# print(max(a , b, c))
#
# # 排序
# list_my = [a, b , c]
# list_my.sort()
# print(list_my[-1])

# # for 循环
# max_num = list_my[0]
# for i in list_my:
#     if i > max_num:
#         max_num = i
# print(max_num)


"""
使用for打印九九乘法表

提示：

输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1
1 * 2 = 2    2 * 2 = 4
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
"""

# for i in [1, 2,3,4,5,6,7,8,9]

# num = 0
# while num <=9

# for i in range(9)
# [0,1,2,...8]
# range(start(0), end , step(1))
# range(0, 9, 1)
# 生成一个数字的类似于列表的东西。

# for i in range(1,10):
#     for j in range(1, 10):
#         if j <= i:
#             print("{} * {} = {}".format(i, j, i*j), end='\t')
#     print()

# for i in range(1, 10):
#     for j in range(1, 10):
#         # 如果 j <= i
#         # if j <= i:
#             print("{} * {} = {}".format(j, i, j *i), end='\t')
#     print()
#
for i in range(1, 10):
    for j in range(1, i + 1):
            print("{} * {} = {}".format(j, i, j *i), end='\t')
    print()

# 特征：
# range(1,9)
# 同时取出 2 个数字，去进行操作。 for..for..
# [1,5,6,7, 8,], for...for...
