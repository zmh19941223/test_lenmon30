import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from task_13day import test_register

import os
# 获取当前用例文件所在的目录
base_dir = os.path.dirname(os.path.abspath(__file__))


# 添加所有的用例
loader = unittest.TestLoader()
s = loader.discover(base_dir)

from BeautifulReport import BeautifulReport

br = BeautifulReport(s)
br.report("py30期-注册功能-测试报告",filename="report_of_register.html")


# # 生成html文件的的测试报告
# runner = HTMLTestRunner(stream=open('report.html', 'wb'),
#                         title='柠檬班测试报告',
#                         description='这是我们30期的第一次生成报告的作业',
#                         tester='Simple_Small')
#
# runner.run(s)
