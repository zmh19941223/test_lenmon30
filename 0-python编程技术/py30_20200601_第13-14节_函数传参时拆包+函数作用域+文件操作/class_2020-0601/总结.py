"""
======================
Author: 柠檬班-小简
Time: 2020/6/1 22:03
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
返回值？？？
函数调用时，传参！！
拆包：把列表/字典/元组  拆成多个值。
列表/元组: *列表/元组   []()
字典：**字典   key=value  key=value  key=value

变量的作用域：
  没有讲函数的时候，没有讲作用域！！！
  有变量，封装在函数内部，仅函数可见！！！ --- 局部变量。
  在py文件当中，在函数之外定义的变量。  --- 全局变量。整个py文件内都可以用。
                                     函数也可以使用。但是函数内部要修改全局变量时，要使用global.
            
  
内置函数
"""

"""
文件操作：打开、读、写、追加、关闭。
open函数：文件路径、打开模式(读写追加)、编码格式
读：read、readlines  -- 文件一定要存在。
写: write （写、追加） --  自己主动加\n换行。  文件可以不存在，会创建。但是路径一定要存在。
关闭：close

资源在使用之后，一定要释放。使用close()关闭释放。
用法： with  open()  as fs:
          文件操作(read,write..)。
"""