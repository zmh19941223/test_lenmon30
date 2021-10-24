"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""

"""
类和对象知识应用：

实现文字版游戏：坦克大战
步骤一：定义TANK类（必做）：
    1、实现一个BaseTank类（所有Tank的父类）
    BaseTank拥有live属性（这个属性代表Tank是否存活 : 1代表活的，0代表死）
    BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有
    （1,10）10个位置）
    BeseTank拥有HP属性（代表血量，默认为10）
    BeseTank拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）
    10个位置）

2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
    move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之
    后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理
    无效数据）
    attack方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提
    示用户重新输入，通过异常来处理无效数据）
    
3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
    move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
    attack方法：发射子弹，攻击目标位置随机生成（1,10）
    
步骤二：游戏规则逻辑完善（扩展题做，不要求提交）
    1、启动游戏后，创建一个玩家坦克，一个电脑tank,
    2、游戏环节（循环，直到有tank死亡才退出循环）
        1、玩家移动、电脑移动
        2、玩家发生子弹，然后电脑坦克发射子弹，
        3、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
        4、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续
        游戏。
        



"""
import random


class BaseTank:

    def __init__(self):
        self.live = 1
        self.position = None
        self.hp = 10
        self.attck_position = None


class MyTank(BaseTank):

    def move(self):
        print("玩家开始移动，请输入移动位置。")
        position = self.__check_data_valid("移动")
        if position:
            self.position = position

    def attack(self):
        print("玩家开始攻击，请输入攻击位置。")
        position = self.__check_data_valid("攻击")
        if position:
            self.attck_position = position

    @staticmethod
    def __check_data_valid(what):
        while True:
            pos = input("请输您的{}位置(0-10): ".format(what))
            try:
                position = int(pos)
                if position in range(1, 11):
                    return position
            except:
                print("输入位置错误，请重新输入！")


class PCTank(BaseTank):
    def move(self):
        print("电脑开始移动")
        self.position = random.randint(1,10)
        # print("电脑移动到: {}".format(self.position))   隐藏电脑的移动位置，玩家靠猜电脑移动在哪里

    def attack(self):
        print("电脑开始攻击")
        self.attck_position = random.randint(1,10)
        print("电脑攻击玩家的位置: {}".format(self.attck_position))


if __name__ == '__main__':
    print("游戏正式开始！！创建玩家对象，和电脑对象！")
    user = MyTank()
    pc = PCTank()

    # 每击中一次，少一滴血。看谁先阵亡。当攻击的位置与对方的位置一样时，对方少一滴血。
    # 一共10滴血，如果被攻击10次，阵亡。游戏结束
    while True:
        if user.hp == 0:
            print("游戏结束，玩家阵亡！")
            break
        if pc.hp == 0:
            print("游戏结束，玩家赢了！")
            break

        # 玩家和电脑各自移动一次
        user.move()
        pc.move()

        # 玩家开始攻击
        user.attack()
        if user.attck_position == pc.position:
            pc.hp -= 1
            print("电脑被击中一次，血量少一滴！目前血量为：{}".format(pc.hp))

        # 电脑开始攻击
        pc.attack()
        if pc.attck_position == user.position:
            user.hp -= 1
            print("玩家被击中一次，血量少一滴！目前血量为：{}".format(user.hp))


