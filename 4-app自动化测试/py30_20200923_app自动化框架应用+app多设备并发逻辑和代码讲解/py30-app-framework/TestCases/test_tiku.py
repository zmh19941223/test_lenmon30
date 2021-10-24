"""
======================
Author: 柠檬班-小简
Time: 2020/9/23 20:11
Project: py30-app-framework
Company: 湖南零檬信息技术有限公司
======================
"""
"""
查看和关闭答案

前置 - 打开app登陆
步骤 - 1、随机选当前页面的题库类型 - 随机选题库难度 - 随机选套题 - 进入到题目页面
      2、点击答案的按钮 - 断言：答案元素是否存在。
      3、点击答案的按钮 - 断言：答案元素不存在。


"""
class TestAnswer:

    def test_into_topic_page(self):
        pass

    def test_open_answer(self):
        pass

    def test_close_anwser(self):
        pass

    # def test_add_favirate(self):
    #     pass
    #
    # def test_cancel_favirate(self):
    #     pass


class TestFavirate:

    def test_into_topic_page(self):
        pass

    def test_add_favirate(self):
        # 获取收藏的题目内容
        # 添加收藏
        # start_activity直接回到主页
        # 判断用户收藏的个数，是否为1
        # 进入收藏列表，进入收藏题目，判断收藏的题目内容是否一致
        pass

    def test_cancel_favirate(self):
        pass
