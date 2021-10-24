"""
======================
Author: 柠檬班-小简
Time: 2020/6/6 14:09
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
使用循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局
提示：电脑随机出拳
使用随机数，首先需要导入随机数的模块 —— “工具包”
import random
导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
random.randint(a, b)，返回[a, b]之间的整数，包含a和b

重复的部分：
    我出一个拳
    电脑出个拳
    谁赢谁输？

当我出4的时候，不玩了！

while True：
    当我出4的时候，不玩了！
    
    我出一个拳(input)
    电脑出个拳（random）
    谁赢谁输？(怎么判断谁赢谁输？)
    
    

(怎么判断谁赢谁输？)  
赢：
你：石头1    电脑：剪刀 2  (1,2)
你：剪刀2    电脑：布3   (2,3)
你：布3    电脑：石头1   (2,3)

平局：
你：石头1    电脑：石头1
你：剪刀2    电脑：剪刀2
你：布3    电脑：布3


  
"""
import random


def get_result(user,computer):
    if (user,computer) in [(1,2),(2,3),(2,3)]:
        return "胜利"  # 赢
    elif (user,computer) in [(1,1),(2,2),(3,3)]:
        return "平局"  # 平局
    else:
        return "输了"  # 输


desc = {"1":"石头","2":"剪刀","3":"布"}

while True:
    user_num = input("输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）")
    if user_num == "4":
        break
    # 电脑出拳
    computer_num = random.randint(1,3)
    # 判断结果
    res = get_result(int(user_num),computer_num)
    print("您的出拳为：{}，电脑出拳为：{}，结果为{}".format(desc[user_num],desc[str(computer_num)],res))







