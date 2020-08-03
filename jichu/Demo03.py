# ！/usr/bin/python3.6
#创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
#与字符串的索引一样，列表索引从0开始，列表可以进行截取、组合
list1 = ['A', 'B', 'C', 'D']
list2 = [1, 2, 3, 4, 5]
list3 = [6, 7, 'E', 'F']
# 访问列表中的值
print("list[0]:", list1[0])
print('list[0]:', list2[0])

# 更新列表
list4 = ['百度', '搜狐']
list4[0] = '阿里巴巴'
print('list4[0]=', list4[0])

# 删除列表元素
list5 = ['我', '和', '们', '都']
# 删除第二个元素
del list5[1]
print('删除第二个元素：', list5)

# 列表拼接
list6 = list4 + list5
print('list6:', list6)

# 列表嵌套
list7 = [['a', 'b', 'c'], [1, 2, 3]]
# 输出['a', 'b', 'c']
print(list7[0])
# 输出 a
print(list7[0][0])
# 在列表末尾添加新的元素
list7.append(['一', '二', '三'])
# list7: [['a', 'b', 'c'], [1, 2, 3], ['一', '二', '三']]
print('list7:', list7)
# 反向列表中元素
list7.reverse()
# 复制列表
list7.copy()
# 清空列表
list7.clear()
