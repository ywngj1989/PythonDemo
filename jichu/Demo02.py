# !/user/bin/python3.6
# 等号（=）用来给变量赋值
# 等号（=）运算符左边是一个变量名，等号（=）运算符右边是存储在变量中的值。例如：
counter = 100 # 整型变量
miles = 100.0 # 浮点型变量
name = "张三" # 字符串
print(counter)
print(miles)
print(name)

#多个变量赋值，python允许你同时为多个变量赋值，例如：
a = b = c = 1
print(a)
print(b)
print(c)

#也可以为多个对象指定多个变量，例如：
a, b, c = 1, 2, "zifuchuan"
print(a)
print(b)
print(c)

# python3中有六个标准的数据类型
# Number（数字）
# String（字符串）
# List(列表)
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# python3的六个标准数据类型中：
# 不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）

# 用type和isinstance来查询变量所指的对象类型
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
a = 123
print(type(a)) #输出<class 'int'>
print(isinstance(a, int)) #输出True或者False