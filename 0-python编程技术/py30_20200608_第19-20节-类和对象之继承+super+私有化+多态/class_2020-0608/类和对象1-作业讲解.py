"""
======================
Author: 柠檬班-小简
Time: 2020/6/8 19:43
Project: py30
Company: 湖南零檬信息技术有限公司
======================
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

class People:

    def eat(self):
        print("吃吃吃！！！！")

class Student:

    identity = "学生"

    def __init__(self,name,age,sex,en_score,math_score,ch_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.en_score = en_score
        self.math_score = math_score
        self.ch_score = ch_score
        # self.identity = "nmb_stu"

    def get_all_score(self):
        # self.all_score = self.ch_score + self.math_score + self.en_score
        return self.ch_score + self.math_score + self.en_score

    def get_avrage_score(self):
        return self.get_all_score() / 3

    def print_stu_info(self):
        print("我的名字叫{}，年龄：{},性别：{}".format(self.name,self.age,self.sex))

    # def print_score(self):
    #     print(self.all_score)

    def who_eat(self,obj): # obj是另外一个类的对象。而且这个对象要具备eat方法。
        print("调用其它类对象的方法。调用People对象的eat方法")
        obj.eat()

xj = Student("小简", 18, "女", 120, 100, 108)
xj.get_all_score()

pp = People()
xj.who_eat(pp)  # 参数是另外一个类的对象。
