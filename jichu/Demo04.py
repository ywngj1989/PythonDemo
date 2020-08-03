#!/usr/bin/python3.6
"""
元组与列表类似，不同之处在于元组的元素不能修改
元组使用小括号()，列表使用方括号[]
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
"""
tup1 = ('google', 'runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6)
# 打印出元组中的最大值
print("max(tup2)=", max(tup2))
# 打印出元组中的最小值
print("min(tup2)=", min(tup2))
# 打印出元组的长度
print("len(tup2)=", len(tup2))
# 不需要括号也可以
tup3 = "a", "b", "c", "d"

# 创建空元组
tup3 = ()

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则会被当作运算符使用
tup4 = (20)
# 不加逗号，类型为整型
# <class 'int'>
type(tup4)

tup5 = (20,)
#加上逗号，类型为元组<class 'tuple'>
type(tup5)

# 访问元组
tup6 = ('alibaba', 'tengxunkeji', 'baidu', 12)
print("tup6[0]=", tup6[0])
print("tup6[1:3]=", tup6[1:3])
"""
修改元组，元组中的元素值是不允许修改的，但可以对元组进行连接组合，如下实例
"""
tup7 = tup6 + tup5
print("tup7=", tup7)



"""
删除元组：元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组，如下实例
"""
tup8 = ('湖北', '上海', '湖南', 330100, 112000)
print(tup8)
del tup8
# tup8 被删除后，下面这个语句会报错
# print("tup8=", tup8)
