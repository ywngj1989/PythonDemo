# !/usr/bin/python
"""
字典是另一种可变容器模型，且可存储任意类型对象
字典的每个键值（key==>value）对用冒号(:)分割，每个对象之间用（,）分割，整个字典包括在花括号{}，中，格式如下：
d = {key1 : value1, key2 : value2}
键必须是唯一的，键不可重复，值可重复
值可以取任何数据类型，但键必须是不可变的，如字符串、数字或元组
"""
dict1 = {'Alice': '2341' , 'Beth': '9102'}
dict2 = {'abc': 23}
dict3 = {'abc': 123, 98.12: 123, 91: 12, 'er': 'jj'}

# 访问字典里的值
print("dict3['abc']=", dict3['abc'])

# 修改字典
dict3[98.12] = 456
print("dict3[98.12]=", dict3[98.12])

# 删除字典元素，能删除单一的元素也能清空字典
# 删除键'abc'
del dict3['abc']
# 清空字典
dict3.clear()
# 删除字典
del dict3

# 字典内置函数和方法
# 计算字典元素个数，即键的总数
len(dict1)
# 输出字典
str(dict1)

# 返回输入的变量类型，如果变量是字典就返回字典类型
type(dict1)
