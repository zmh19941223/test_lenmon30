#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/11/28 14:27
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
1、.删除如下列表中的"矮穷丑"，写出能想到的所有方法



info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]


- `info.remove("矮穷丑")`
- `info.pop(3)` 或者`keyou_info.pop(-5)`
- del keyou_info[3]` 或者`del keyou_info[-5]`,
"""


"""

2、有5道小题：
a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄

b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；

c, 平台为了保护你的隐私，需要你删除你的联系方式；

d, 你为了取得更好的成绩，需要取一个花名， 并修改自己的身高和其他你觉得需要改的信息。

e, 你进一步添加自己的兴趣，至少需要 3 项。

锻炼解决问题能力，把需求转化成代码
"""
# 列表
# user_info = ['yuze', '男', 18]
# user_info.append(180)
# user_info.append()
# user_info.insert()
# user_info.extend([180, '18173179913'])
# user_info.pop(3)
# user_info.append('雨泽哥哥')
# 修改
# user_info[index] = 'value'
# user_info[1] = '女'
# # 不可变类型
# user_info.append(['唱歌', '跳舞', '睡觉'])
# user_info.append('唱歌，跳舞，睡觉')
#
# # 下节课讲字典 还没学操作
# user_info = {"name": "yuze", "gender": "男", "age": 18}
# user_info['height'] = 185
# user_info['mobile'] = '18173179913'
# user_info.pop('mobile')
# user_info['nick_name'] = '雨泽哥哥'
# user_info['gender'] = '女'
# user_info['hobby'] = '唱歌，跳舞，睡觉'


"""
3、现在有一个列表 li2=[1，2，3，4，5]，


     第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，

     第二步：对li2进行排序处理 

    第三步：请写出删除列表中元素的方法，并说明每个方法的作用
"""

li2 = [1, 2, 3, 4, 5]
li2.insert(0, 0)
li2.insert(4, 66)
li2.extend([11, 22, 33])


# 排序
li2.sort(reverse=True)

print(li2)