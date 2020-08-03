#!/usr/bin/python3.6
# 这里主要是python基本语法
# 第一个注释
print("Hello, python")# 第二个注释
'''
这是一个多行注释
'''
"""
这是第二个多行注释
"""
print("这是我的第一个python测试")
str1 = '湖北'
str2 = '武汉'
str3 = '加油'
#python中用反斜杠(\)实现多行语句
str4 = str1+\
       str2+\
       str3
print(str4)
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

#Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
str='这是一个字符串'
print(str)

#字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
str5=str[0:3]#截取第一位到第三位的字符
print("str5=",str5)
str6=str[:]#截取字符串的全部字符
print("str6=",str6)
str7=str[5:]#从第五个字符开始截取（不包括第五个字符）
print("str7=",str7)
str8=str[:-2]#截取从头开始到倒数第二个字符之前
print("str8=",str8)
str9=str[2]#截取第三个字符
print("str9=",str9)
str10=str[-1]#截取倒数第一个字符
print("str10=",str10)
str11=str[::-1]#创建一个与原字符串顺序相反的字符串
print("str11=",str11)
str12=str[-3:-1]#截取倒数第三位与倒数第一位之前的字符
print("str12=",str12)
str13=str[-3:]#截取倒数第三位到结尾
print("str13=",str13)

x=2
y=3
#换行输出
print(x)
print(y)

#不换行输出
print(x,end=" ")
print(y,end=" ")
