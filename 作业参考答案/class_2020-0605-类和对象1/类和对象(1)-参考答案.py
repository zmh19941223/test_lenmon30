"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""

"""
1、类属性怎么定义？ 实例属性怎么定义？

在类当中，直接定义：属性名=值
在类的方法当中：self.属性名=值

若类属性和实例属性同名，在实例对象当中，对象名.属性名调用的是 对象自己的属性。
自己有，用自己的。
自己没有，用类的。

"""


"""    
2、实例方法中的self代表什么？（简答）
self代表对象本身。
在实例化的对象是谁，self就是谁。
     
3、类中__init__方法在什么时候会调用的？（简答）
__init__方法，在实例化对象时，自动调用。


"""

"""
4、定义一个登录的测试用例类Case
属性：用例名称   用例步骤    预期结果   实际结果
方法：运行用例、用例结果(比对预期结果和实际结果是否相等)
实例化2个测试用例 ，并运行用例(调用方法) ，呈现用例结果(调用方法)
"""
class Case:

    user = "xiaojian"
    passwd = "888888"

    def __init__(self,name,user,passwd,expected):
        self.case_name = name
        self.case_user = user
        self.case_passwd = passwd
        self.case_expected = expected
        self.case_actual = None

    def run_case(self):
        print("运行测试用例：{}，".format(self.case_name))
        if self.user == self.case_user and self.passwd == self.case_passwd:
            self.case_actual = "登陆成功"
        else:
            self.case_actual = "登陆失败"

    def case_is_passed(self):
        if self.case_actual == self.case_expected:
            print('用例通过')
        else:
            print("用例失败")


login_case = Case("正常登陆","xiaojian","888888","登陆成功")
login_case.run_case()
login_case.case_is_passed()


login_case2 = Case("登陆-密码错误","xiaojian","1234567","登陆失败")
login_case2.run_case()
login_case2.case_is_passed()


"""
5、封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)

-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
实例化1个学生,并打印学生个人信息，计算总分。
"""

class Student:

    identity = "学生"

    def __init__(self,name,age,sex,en_score,math_score,ch_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.en_score = en_score
        self.math_score = math_score
        self.ch_score = ch_score

    def get_all_score(self):
        return self.ch_score + self.math_score + self.en_score

    def get_avrage_score(self):
        return self.get_all_score() / 3

    def print_stu_info(self):
        print("我的名字叫{}，年龄：{},性别：{}".format(self.name,self.age,self.sex))


xj = Student("小简", 18, "女", 120, 100, 108)
xj.print_stu_info()
print("{}语数外的总分为：{}".format(xj.name,xj.get_all_score()))
print("{}语数外的平均分为：{:.2f}".format(xj.name,xj.get_avrage_score()))

