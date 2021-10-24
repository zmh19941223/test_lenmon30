"""
 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典

加入默认参数的情况， values()

# key 保持不可变类型，并且是唯一的。
"""
import random

def add_element(e, mdict={}):
    # TODO: 不要 把 mdict={} 成默认参数
    if e not in mdict.values():
        # e 作为 key
        while True:
            key = random.randint(1, 90000000)
        # 判断 key 是否在 mdict.keys()
            if key not in mdict.keys():
                mdict[key] = e
                break
    return mdict



"""

通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
"""


methods = {'1':'+', '2': '-', '3': '*', '4': '/'}

def calc(x, y, method):
    # methods['1']  + - * /
    method_f = methods[method] #
    # 字符串转化成可以运行的 python 代码
    # 3 + 4
    return eval("{} {} {}".format(x,method_f,y))

method = input("运算符：")
print(calc(3.1, 4, method))




"""

一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""

def join_team(age):
    """shifou 可以加入足球"""
    if 15 <= age <= 22:
        return True
    return False
#

def main():
    """主程序"""
    num = 0
    for i in range(3):
        age = input('输入年龄：')
        # 做
        if not age.isdigit():
            print("输入不合法。")
            continue
        joined = join_team(int(age))
        if joined:
            num += 1
    print(num)


"""
第二题：数据转换

# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# 要求一：把上述数据转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
"""


def transform(cases):
    # if type(cases) != list:
    # 判断类型的

    if not isinstance(cases, list):
        print("不是 list")
        return

    new_cases = []

    title = cases[0]

    for case in cases[1:]:
        # [1, '用例1', 'www.baudi.com', '001', 'ok'],   ['case_id', 'case_title', 'url', 'data', 'excepted'],
        # {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
        dict_case = {}
        # 可以同时获取索引和值
        for i, column in enumerate(case):
            # 0, 1
            # dict_case['case_id'] = 1
            # dict_case['case_title'] = '用例1'
            dict_case[title[i]] = column
        new_cases.append(dict_case)
    return new_cases


def transform_zip(cases):
    if type(cases) != list:
        print("不是 list")
        return

    new_cases = []
    title = cases[0]
    for i in cases[1:]:
        # title = ['case_id', 'case_title', 'url', 'data', 'excepted']
        # i = [1, '用例1', 'www.baudi.com', '001', 'ok']
        # [(case_id, 1), (case_title, '用例1'), (url, 'wwww.)]
        # zip
        new_dict = dict(zip(title, i))
        new_cases.append(new_dict)
    return new_cases


def filter(cases, id):
    new_cases = []
    for c in cases:
        if c['case_id'] > id:
            new_cases.append(c)
    return new_cases


cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# a = transform(cases)
# print(a)
# print(filter(a, 3))
# print(transform_zip(cases))

if __name__ == '__main__':
    a = transform(cases)
    print(a)

    b = filter(a, 3)
    print(b)
