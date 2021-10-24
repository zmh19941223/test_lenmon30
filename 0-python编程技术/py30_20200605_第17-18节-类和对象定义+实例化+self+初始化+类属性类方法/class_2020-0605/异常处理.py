"""
======================
Author: 柠檬班-小简
Time: 2020/6/5 20:13
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
try:
    代码
except 异常名字:
    处理代码
except 异常名字:
    处理代码
except 异常名字:
    处理代码
except Exception as e:
    pass


"""

try:
    fs = open(r"D:\Pychram-Workspace\py30\python练习.txt","r",encoding="utf-8")
except FileNotFoundError as e:
    print("文件找不着！！文件不存在！！")
    # print(e)
    raise
except KeyError:
    print("另外的异常，key错误！！")
except Exception:
    print("不是FileNotFoundError,也不是KeyError，是另外一种Error!!")