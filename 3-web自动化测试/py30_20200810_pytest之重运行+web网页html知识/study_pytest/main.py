"""
======================
Author: 柠檬班-小简
Time: 2020/8/3 21:07
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
生成html报告的时候：
1、安装html插件：pip install pytest-html
2、在运行用例的时候，添加参数：--html=html的路径(相对于rootdir)

"""

import pytest

# pytest.main(["-s","-v",
#              "-m","demo",
#              "--html=report.html",
#              "--alluredir=allure_dir"])  #  收集所在目录下的所有用例并执行。


# 运行一个即有smoke标签又有demo标签的用例。
# pytest.main(["-s","-v",
#              "-m smoke and demo",
#              "--html=report.html",
#              "--alluredir=allure_dir"])  #  收集所在目录下的所有用例并执行。

pytest.main(["-s","-v",
             "-m","py30",
             "--html=report.html",
             "--alluredir=allure_dir",
             "--reruns","2","--reruns-delay","5"])