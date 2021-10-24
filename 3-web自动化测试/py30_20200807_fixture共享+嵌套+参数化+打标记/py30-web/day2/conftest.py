"""
======================
Author: 柠檬班-小简
Time: 2020/8/7 20:13
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、放的都是fixture
2、fixtures可以对外共享。
3、共享的范围：
   当前conftest.py所在目录下的(含子孙目录)，所有用例共享 
4、conftest.py，是可以创建多个，在不同的包下。可以层级创建的。
5、优先级：就近原则！！
    发现fiXture: 用例自己的模块 -》用例所在目录下的conftest.py -》目录的父级目录下的conftest.py

6、嵌套方式：
   6.1 什么时候嵌套？  一个fixture，想完全使用另外一个fixture,并在人家的基础上新增一些代码。
   6.2 怎么嵌套？  
       @pytest.fixture
        def fix1():
            pass
        
        @pytest.fixture
        def fix2(fix1):
            # 新增的代码
            pass
   6.3 嵌套后的执行顺序？
       fix1 的前置 
       fix2 的前置
       fix2 的后置 
       fix1 的后置
       
   6.4 可以任意fixture级别嵌套吗？
       fix1 >= fix2的级别
   

day2包下面的conftest.py


"""
import pytest


@pytest.fixture    # setup,teardown
def root():
    print(" 项目根目录下的conftest.py  作用域为测试函数的 **** 前置代码")
    yield True,100
    print(" 项目根目录下的conftest.py  作用域为测试函数的 **** 后置代码")


@pytest.fixture
def init2(root):  # 直接使用root这个fiXture的前置后置，返回值。在它的基础上，增加一些内容。
    print(" 增加的：day2包下的conftest.py  作用域为测试函数的 **** 前置代码")
    yield root
    print(" 增加的：项目根目录下的conftest.py  作用域为测试函数的 **** 后置代码")


# @pytest.fixture    # setup,teardown
# def init():
#     print(" 项目根目录下的conftest.py  作用域为测试函数的 **** 前置代码")
#     print(" 增加的：day2包下的conftest.py  作用域为测试函数的 **** 前置代码")  # 增加的
#     yield True,100
#     print(" day2包下的conftest.py  作用域为测试函数的 **** 后置代码")
#     print(" 增加的：项目根目录下的conftest.py  作用域为测试函数的 **** 后置代码") # 增加的

"""
root的前置
init2的前置

init2的后置
root的后置
"""



@pytest.fixture(scope="class")  # setupClass,setupTeardown
def class_fix():
    print(" 作用域为测试*** 类 **** 前置代码")
    yield "I am class"
    print(" 作用域为测试函*** 类 **** 后置代码")
