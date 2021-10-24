"""
======================
Author: 柠檬班-小简
Time: 2020/6/6 14:10
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
[1,4,7,34,2,89]
[1, 4, 7, 34, 2]
[1,4,7,2]
[1,4,2]
[1,2]

for j in range(len(a)-1):
    print(j)
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    print(a)
"""



# def is_one_of_ball(age,sex):
#     if 15<= age <= 22 and sex == "女":
#         return True
#     else:
#         return False
#
#
# count = 0
# for index in range(10):
#     sex = input("请输入性别")
#     age = input("请输入年龄")
#     # 确认此人是否可以加入球队，可以则返回True,不可以返回False
#     res = is_one_of_ball(int(age),sex)
#     if res is True:
#         count += 1
# print(count)
