"""
1、现在有字符串：str1 = 'python cainiao 666'


1、请找出第 5 个字符。
2、请复制一份字符串，保存为 str_two
3、请找出最中间的字符。（字符串长度是偶数。）
"""
str1 = 'python cainiao 666'

# 请找出第 5 个字符。
# print(str1[4])


# 请复制一份字符串，保存为 str_two
# str_two = str1


# 请找出最中间的字符。（字符串长度是偶数。)
# 获取字符串长度，除以2。因为是偶数，没有绝对意义上的中间。所以中间的2个数取其中1个都可以。
middle = int(len(str1) / 2 )
# print(str1[middle - 1])  # 答案可以是这个
# print(str1[middle])  # 答案也可以是这个





"""卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。） """

# price = input("价格：")
# weight = input("重量：")
# # input 得到的数据类型是：：：永远都是 str
# print( float(price) * float(weight) )


"""
my_hobby = "Never stop learning!"
"""

my_hobby = "Never stop learning!"
# 位置2 - 位置6   --- 取下标为：1，2，3，4，5的值
print(my_hobby[1:6])

# 截取从 开始位置~ 位置6 的字符串    --- 取下标为：0，1，2，3，4，5的值
print(my_hobby[:6])

# 开始到最后
print(my_hobby[:])


# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3: : 2])

# 从右边开始截取，倒数第 2位置 到 倒数 5位置，步长为2
# 倒序取值。从下标-2开始，在-2，-3，-4，-5 中取 -2，-4
print(my_hobby[-2: -6 : -2])

 # 截取字符串末尾两个字符
print(my_hobby[-2:])

# TODO: 字符串的逆序
print(my_hobby[::-1])



