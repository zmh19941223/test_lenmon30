# #########################################
# # 定义函数：将用户输入的所有数字相乘之后对20取余数
# # 用户输入的数字个数不确定
# #########################################
# def multiply_module(numbers):
#     """很多数据相乘 % 20.
#     numbers: 列表
#     """
#     start_number = 1
#     for i in numbers:
#         start_number *= int(i)
#     module = start_number % 20
#     return module
#
# input_numbers = input("请输入所有的数字，以逗号隔开：（4, 5, 6）")
# numbers = input_numbers.split(',')
# print(multiply_module(numbers))


# ##################################################
# # 编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# #################################################
# def check_list(some_list):
#     """检查某个列表的长度。
#     some_list
#     """
#     if len(some_list) > 2:
#         return some_list[:2]


# ###################################3
# ## 列表去重
# ## 定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# #################################
# def remove_element(m_list):
#     """去除某列表的重复元素"""
#     return list(set(m_list))


# ###########################
# """
# 编写如下程序
#
# 尝试函数封装：
#
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
#
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
#
# b.根据BMI指数，给与相应提醒
# """
# #############################
#
# def get_bmi(height, weight):
#     """计算bmi, 根据身高和体重
#     身高（单位m)
#     体重（单位kg)
#     """
#     bmi = weight / height ** 2
#     if bmi < 18.5:
#         return "太轻"
#     elif  18.5 < bmi < 25:
#         return "正常"
#     elif 25 < bmi < 28:
#         return "肥胖"
#     else:
#         return "太胖"
#
# h = 1.65
# w = 66
# res = get_bmi(h,w)
# print("得到的结果：{}".format(res))